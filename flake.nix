{
  description = "Public StarIntel actor documentation and scaffold checks (no actor runtime)";

  # Exact nixos-25.11 revision; the lock also records the archive content hash.
  inputs.nixpkgs.url = "https://github.com/NixOS/nixpkgs/archive/b6018f87da91d19d0ab4cf979885689b469cdd41.tar.gz";

  outputs = { self, nixpkgs }:
    let
      # Only this platform is advertised until another has execution evidence.
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      docs = pkgs.runCommand "starintel-actors-docs" { } ''
        root="$out/share/starintel-actors"
        mkdir -p "$root/actors" "$root/scripts"
        cp ${./README.md} "$root/README.md"
        cp ${./AGENTS.md} "$root/AGENTS.md"
        cp ${./actors/README.md} "$root/actors/README.md"
        cp -r ${./actors/symbolic-investigation} "$root/actors/"
        cp -r ${./docs} "$root/docs"
        cp ${./scripts/check_docs.py} "$root/scripts/check_docs.py"
      '';
      docsCheck = pkgs.writeShellApplication {
        name = "starintel-actors-check-docs";
        runtimeInputs = [ pkgs.python3 ];
        text = ''
          exec python3 -B ${docs}/share/starintel-actors/scripts/check_docs.py
        '';
      };
    in
    {
      packages.${system} = {
        inherit docs;
        docs-check = docsCheck;
        default = docs;
      };

      apps.${system} = {
        docs-check = {
          type = "app";
          program = "${docsCheck}/bin/starintel-actors-check-docs";
        };
        default = self.apps.${system}.docs-check;
      };

      checks.${system} = {
        documentation = pkgs.runCommand "starintel-actors-documentation-check" { } ''
          ${docsCheck}/bin/starintel-actors-check-docs
          touch "$out"
        '';
        documentation-gate = pkgs.runCommand "starintel-actors-documentation-gate-tests" {
          nativeBuildInputs = [ pkgs.python3 ];
        } ''
          python3 -B -m unittest discover -s ${./.}/scripts -p 'test_*.py' -v
          touch "$out"
        '';
      };
    };
}

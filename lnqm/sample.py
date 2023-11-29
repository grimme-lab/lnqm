from pydantic import BaseModel
from torch import Tensor


class LnQM_Sample(BaseModel):
    """
    Data model representation for samples in the `LnQM` dataset.

    While designed for comprehensive representation, some attributes
    may contain redundant information. For instance:
    - Total electron count (`nel`) can be deduced from alpha (`nel_alpha`)
      and beta (`nel_beta`) electron counts.
    - The combined exchange-correlation energy (`exc`) is the sum of
      exchange (`ex`) and correlation (`ec`) energies.
    - The Mulliken charges are encompassed within Mayer population.

    Units:
    All numerical attributes are expressed in atomic units (Hartree, Bohr, etc.).
    """

    class Config:
        arbitrary_types_allowed = True

    # General properties
    uid: str
    """Unique identifier for the calculation."""

    time_singlepoint: Tensor
    """Time taken for the singlepoint ORCA calculation in seconds."""

    time_geoopt: Tensor
    """Time taken for the geometry optimization ORCA calculation in seconds."""

    # Geometric properties
    numbers: Tensor
    """Atomic numbers."""

    coord: Tensor
    """Optimized geometry in Bohr."""

    gradient: Tensor
    """Gradient of the optimized geometry in Eh/Bohr."""

    trajectory: Tensor
    """Trajectory of atomic positions during optimization in Bohr."""

    trajectory_energies: Tensor
    """Energies at different points in the optimization trajectory in Eh."""

    trajectory_etot: Tensor
    """Energies without dispersion correction at different points in the optimization trajectory in Eh."""

    trajectory_gradients: Tensor
    """Gradients at different points in the optimization trajectory in Eh/Bohr."""

    cn: Tensor
    """Coordination numbers from D4 calculation."""

    # Energetic properties
    energy: Tensor
    """Total single point energy from the ORCA calculation in Eh."""

    energy_geoopt: Tensor
    """Energy after geometric optimization in Eh. This is important for comparability with other trajectory features."""

    etot_geoopt: Tensor
    """Energy after geometric optimization without dispersion correction in Eh. This is important for comparability with other trajectory features."""

    ex: Tensor
    """Exchange energy in Eh."""

    ec: Tensor
    """Correlation energy in Eh."""

    exc: Tensor
    """Exchange-correlation energy in Eh."""

    ecnl: Tensor
    """Non-local correlation energy in Eh."""

    eemb: Tensor
    """Embedding correction energy in Eh."""

    homo_spin_up: Tensor
    """HOMO energy for spin-up electrons in Eh."""
    # NOTE: SOMO for alpha spin channel in open shell systems

    lumo_spin_up: Tensor
    """LUMO energy for spin-up electrons in Eh."""

    homo_spin_down: Tensor
    """HOMO energy for spin-down electrons in Eh."""
    # NOTE: SOMO for beta spin channel in open shell systems

    lumo_spin_down: Tensor
    """LUMO energy for spin-down electrons in Eh."""

    orbital_energies_spin_up: Tensor
    """Energies of orbitals for spin-up electrons in Eh."""

    orbital_energies_spin_down: Tensor
    """Energies of orbitals for spin-down electrons in Eh."""

    # Electronic properties
    charge: Tensor
    """Total charge of the molecule in e."""

    unpaired_e: Tensor
    """Number of unpaired electrons."""

    nel_alpha: Tensor
    """Number of alpha electrons."""

    nel_beta: Tensor
    """Number of beta electrons."""

    nel: Tensor
    """Total number of electrons."""

    polarizabilities: Tensor
    """Polarizabilities from D4 calculation."""

    eeq: Tensor
    """EEQ charges from tblite calculation in e."""

    ceh: Tensor
    """CEH charges from tblite calculation in e."""

    q_gfn2: Tensor
    """Charges from GFN2 calculation in e."""

    # Population and bond properties
    mayer_pop: Tensor
    """Mayer population analysis values.
        Sorted by:
            NA   - Mulliken gross atomic population
            ZA   - Total nuclear charge
            QA   - Mulliken gross atomic charge
            VA   - Mayer's total valence
            BVA  - Mayer's bonded valence
            FA   - Mayer's free valence
    """

    mayer_bo: Tensor
    """Mayer bond order values with tuple indices.
        Sorted by:
            Atom idx A - idx of atom A
            Atom idx B - idx of atom B
            Bond order - value of bond order
    """

    loewdin_charges: Tensor
    """Loewdin atomic charges."""

    loewdin_spins: Tensor
    """Loewdin spin populations."""

    mulliken_charges: Tensor
    """Mulliken atomic charges."""

    mulliken_spins: Tensor
    """Mulliken spin populations."""

    hirshfeld_charges: Tensor
    """Hirshfeld atomic charges."""

    hirshfeld_spins: Tensor
    """Hirshfeld spin populations."""

    hirshfeld_alpha: Tensor
    """Hirshfeld total integrated alpha density."""

    hirshfeld_beta: Tensor
    """Hirshfeld total integrated beta density."""

    # Molecular properties
    rot_const: Tensor
    """Rotational constants in MHz."""

    rot_dipole: Tensor
    """Dipole components along the rotational axes in A.U.."""

    dipole: Tensor
    """Magnitude of the dipole moment in A.U.."""

    dipole_ele: Tensor
    """Electronic xyz-contribution to the dipole moment."""

    dipole_nuc: Tensor
    """Nuclear xyz-contribution to the dipole moment."""

    dipole_tot: Tensor
    """Total xyz-dipole moment."""

    def __str__(self):
        return f"Sample({self.uid})"

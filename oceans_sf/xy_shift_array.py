import numpy as np


def shift_array2d(  # noqa: D417
    input_array, shift_right=0, shift_down=0, boundary="periodic-all"
):
    """
    Shifts 2D array right and down by the specified integer amounts and returns
    the shifted arrays. Either wraps the array or shifts and pads with NaNs.

    Parameters
    ----------
        input_array: array_like
            2-dimensional array to be shifted.
        shift_right: int, optional
            Shift amount for rightward shift. For periodic data should be less than
            half the row length and less than the row length for other boundary
            conditions. Defaults to 0.
        shift_down: int, optional
            Shift amount for downward shift. For periodic data should be less than
            half the column length and less than the column length for other boundary
            conditions. Defaults to 0.
        boundary: str, optional
            Boundary condition for input array. Periodic boundary conditions will wrap
            the array, otherwise the array will be padded with NaNs. Accepted strings
            are "periodic-x", "periodic-y", and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        xy_shifted_array
            2D array shifted i the x-y directions by the specified integer amount
    """
    xy_shifted_array = np.full(np.shape(input_array), np.nan)

    if boundary == "periodic-all":
        xy_shifted_array[:, :shift_right] = input_array[:, -shift_right:]
        xy_shifted_array[:, shift_right:] = input_array[:, :-shift_right]

        xy_shifted_array[:shift_down, :] = xy_shifted_array[-shift_down:, :]
        xy_shifted_array[shift_down:, :] = xy_shifted_array[:-shift_down, :]

    return xy_shifted_array
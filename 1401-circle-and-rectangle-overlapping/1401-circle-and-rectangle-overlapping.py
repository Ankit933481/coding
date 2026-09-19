class Solution:

  def checkOverlap(
      self,
      radius: int,
      x_center: int,
      y_center: int,
      x1: int,
      y1: int,
      x2: int,
      y2: int,
  ) -> bool:
    # Find closest point on the rectangle to circle center
    closest_x = max(x1, min(x2, x_center))
    closest_y = max(y1, min(y2, y_center))

    # Calculate squared distance
    dx = x_center - closest_x
    dy = y_center - closest_y

    return dx * dx + dy * dy <= radius * radius
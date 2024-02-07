# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSurfacePointsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_coord_list': 'list[float]',
        'y_coord_list': 'list[float]',
        'z_coord_list': 'list[float]'
    }

    attribute_map = {
        'x_coord_list': 'x_coord_list',
        'y_coord_list': 'y_coord_list',
        'z_coord_list': 'z_coord_list'
    }

    def __init__(self, x_coord_list=None, y_coord_list=None, z_coord_list=None):
        """RunSurfacePointsReq

        The model defined in huaweicloud sdk

        :param x_coord_list: x坐标集
        :type x_coord_list: list[float]
        :param y_coord_list: y坐标集
        :type y_coord_list: list[float]
        :param z_coord_list: z坐标集
        :type z_coord_list: list[float]
        """
        
        

        self._x_coord_list = None
        self._y_coord_list = None
        self._z_coord_list = None
        self.discriminator = None

        self.x_coord_list = x_coord_list
        self.y_coord_list = y_coord_list
        self.z_coord_list = z_coord_list

    @property
    def x_coord_list(self):
        """Gets the x_coord_list of this RunSurfacePointsReq.

        x坐标集

        :return: The x_coord_list of this RunSurfacePointsReq.
        :rtype: list[float]
        """
        return self._x_coord_list

    @x_coord_list.setter
    def x_coord_list(self, x_coord_list):
        """Sets the x_coord_list of this RunSurfacePointsReq.

        x坐标集

        :param x_coord_list: The x_coord_list of this RunSurfacePointsReq.
        :type x_coord_list: list[float]
        """
        self._x_coord_list = x_coord_list

    @property
    def y_coord_list(self):
        """Gets the y_coord_list of this RunSurfacePointsReq.

        y坐标集

        :return: The y_coord_list of this RunSurfacePointsReq.
        :rtype: list[float]
        """
        return self._y_coord_list

    @y_coord_list.setter
    def y_coord_list(self, y_coord_list):
        """Sets the y_coord_list of this RunSurfacePointsReq.

        y坐标集

        :param y_coord_list: The y_coord_list of this RunSurfacePointsReq.
        :type y_coord_list: list[float]
        """
        self._y_coord_list = y_coord_list

    @property
    def z_coord_list(self):
        """Gets the z_coord_list of this RunSurfacePointsReq.

        z坐标集

        :return: The z_coord_list of this RunSurfacePointsReq.
        :rtype: list[float]
        """
        return self._z_coord_list

    @z_coord_list.setter
    def z_coord_list(self, z_coord_list):
        """Sets the z_coord_list of this RunSurfacePointsReq.

        z坐标集

        :param z_coord_list: The z_coord_list of this RunSurfacePointsReq.
        :type z_coord_list: list[float]
        """
        self._z_coord_list = z_coord_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunSurfacePointsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

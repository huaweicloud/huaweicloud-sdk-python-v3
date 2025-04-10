# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImmediateEventReferencePath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_path': 'list[ImmediateEventPosition3D]',
        'path_radius': 'int'
    }

    attribute_map = {
        'active_path': 'active_path',
        'path_radius': 'path_radius'
    }

    def __init__(self, active_path=None, path_radius=None):
        r"""ImmediateEventReferencePath

        The model defined in huaweicloud sdk

        :param active_path: **参数说明**：通过点集合定义一个有向的作用范围。
        :type active_path: list[:class:`huaweicloudsdkdris.v1.ImmediateEventPosition3D`]
        :param path_radius: **参数说明**：事件的影响区域半径，可选，单位为分米。用半径表示影响区域边界离中心线的垂直距离，反映该区域的宽度以覆盖实际路段。
        :type path_radius: int
        """
        
        

        self._active_path = None
        self._path_radius = None
        self.discriminator = None

        self.active_path = active_path
        if path_radius is not None:
            self.path_radius = path_radius

    @property
    def active_path(self):
        r"""Gets the active_path of this ImmediateEventReferencePath.

        **参数说明**：通过点集合定义一个有向的作用范围。

        :return: The active_path of this ImmediateEventReferencePath.
        :rtype: list[:class:`huaweicloudsdkdris.v1.ImmediateEventPosition3D`]
        """
        return self._active_path

    @active_path.setter
    def active_path(self, active_path):
        r"""Sets the active_path of this ImmediateEventReferencePath.

        **参数说明**：通过点集合定义一个有向的作用范围。

        :param active_path: The active_path of this ImmediateEventReferencePath.
        :type active_path: list[:class:`huaweicloudsdkdris.v1.ImmediateEventPosition3D`]
        """
        self._active_path = active_path

    @property
    def path_radius(self):
        r"""Gets the path_radius of this ImmediateEventReferencePath.

        **参数说明**：事件的影响区域半径，可选，单位为分米。用半径表示影响区域边界离中心线的垂直距离，反映该区域的宽度以覆盖实际路段。

        :return: The path_radius of this ImmediateEventReferencePath.
        :rtype: int
        """
        return self._path_radius

    @path_radius.setter
    def path_radius(self, path_radius):
        r"""Sets the path_radius of this ImmediateEventReferencePath.

        **参数说明**：事件的影响区域半径，可选，单位为分米。用半径表示影响区域边界离中心线的垂直距离，反映该区域的宽度以覆盖实际路段。

        :param path_radius: The path_radius of this ImmediateEventReferencePath.
        :type path_radius: int
        """
        self._path_radius = path_radius

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
        if not isinstance(other, ImmediateEventReferencePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

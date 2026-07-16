# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrontLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'point_list': 'list[FrontPoint]',
        'group_by': 'str'
    }

    attribute_map = {
        'point_list': 'point_list',
        'group_by': 'group_by'
    }

    def __init__(self, point_list=None, group_by=None):
        r"""FrontLine

        The model defined in huaweicloud sdk

        :param point_list: 趋势图数据
        :type point_list: list[:class:`huaweicloudsdkagentarts.v1.FrontPoint`]
        :param group_by: 分组名
        :type group_by: str
        """
        
        

        self._point_list = None
        self._group_by = None
        self.discriminator = None

        self.point_list = point_list
        if group_by is not None:
            self.group_by = group_by

    @property
    def point_list(self):
        r"""Gets the point_list of this FrontLine.

        趋势图数据

        :return: The point_list of this FrontLine.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.FrontPoint`]
        """
        return self._point_list

    @point_list.setter
    def point_list(self, point_list):
        r"""Sets the point_list of this FrontLine.

        趋势图数据

        :param point_list: The point_list of this FrontLine.
        :type point_list: list[:class:`huaweicloudsdkagentarts.v1.FrontPoint`]
        """
        self._point_list = point_list

    @property
    def group_by(self):
        r"""Gets the group_by of this FrontLine.

        分组名

        :return: The group_by of this FrontLine.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this FrontLine.

        分组名

        :param group_by: The group_by of this FrontLine.
        :type group_by: str
        """
        self._group_by = group_by

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FrontLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataConnectionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_name': 'str',
        'dw_id': 'str',
        'display_name': 'str',
        'dw_type': 'str'
    }

    attribute_map = {
        'dw_name': 'dw_name',
        'dw_id': 'dw_id',
        'display_name': 'display_name',
        'dw_type': 'dw_type'
    }

    def __init__(self, dw_name=None, dw_id=None, display_name=None, dw_type=None):
        r"""DataConnectionVO

        The model defined in huaweicloud sdk

        :param dw_name: 数据连接名称。
        :type dw_name: str
        :param dw_id: 数据连接ID。
        :type dw_id: str
        :param display_name: 数据连接名称，适配现有实现。
        :type display_name: str
        :param dw_type: 数据连接类型。
        :type dw_type: str
        """
        
        

        self._dw_name = None
        self._dw_id = None
        self._display_name = None
        self._dw_type = None
        self.discriminator = None

        if dw_name is not None:
            self.dw_name = dw_name
        if dw_id is not None:
            self.dw_id = dw_id
        if display_name is not None:
            self.display_name = display_name
        if dw_type is not None:
            self.dw_type = dw_type

    @property
    def dw_name(self):
        r"""Gets the dw_name of this DataConnectionVO.

        数据连接名称。

        :return: The dw_name of this DataConnectionVO.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this DataConnectionVO.

        数据连接名称。

        :param dw_name: The dw_name of this DataConnectionVO.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def dw_id(self):
        r"""Gets the dw_id of this DataConnectionVO.

        数据连接ID。

        :return: The dw_id of this DataConnectionVO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this DataConnectionVO.

        数据连接ID。

        :param dw_id: The dw_id of this DataConnectionVO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def display_name(self):
        r"""Gets the display_name of this DataConnectionVO.

        数据连接名称，适配现有实现。

        :return: The display_name of this DataConnectionVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this DataConnectionVO.

        数据连接名称，适配现有实现。

        :param display_name: The display_name of this DataConnectionVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def dw_type(self):
        r"""Gets the dw_type of this DataConnectionVO.

        数据连接类型。

        :return: The dw_type of this DataConnectionVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this DataConnectionVO.

        数据连接类型。

        :param dw_type: The dw_type of this DataConnectionVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

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
        if not isinstance(other, DataConnectionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

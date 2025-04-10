# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteBaseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_id': 'str',
        'ids': 'list[str]'
    }

    attribute_map = {
        'dw_id': 'dw_id',
        'ids': 'ids'
    }

    def __init__(self, dw_id=None, ids=None):
        r"""BatchDeleteBaseDTO

        The model defined in huaweicloud sdk

        :param dw_id: 数据连接id
        :type dw_id: str
        :param ids: id列表
        :type ids: list[str]
        """
        
        

        self._dw_id = None
        self._ids = None
        self.discriminator = None

        if dw_id is not None:
            self.dw_id = dw_id
        if ids is not None:
            self.ids = ids

    @property
    def dw_id(self):
        r"""Gets the dw_id of this BatchDeleteBaseDTO.

        数据连接id

        :return: The dw_id of this BatchDeleteBaseDTO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this BatchDeleteBaseDTO.

        数据连接id

        :param dw_id: The dw_id of this BatchDeleteBaseDTO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def ids(self):
        r"""Gets the ids of this BatchDeleteBaseDTO.

        id列表

        :return: The ids of this BatchDeleteBaseDTO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchDeleteBaseDTO.

        id列表

        :param ids: The ids of this BatchDeleteBaseDTO.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, BatchDeleteBaseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

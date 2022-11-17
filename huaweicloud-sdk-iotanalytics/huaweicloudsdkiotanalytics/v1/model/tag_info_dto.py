# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator_id': 'str',
        'data_store_id': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'operator_id': 'operator_id',
        'data_store_id': 'data_store_id',
        'tag': 'tag'
    }

    def __init__(self, operator_id=None, data_store_id=None, tag=None):
        """TagInfoDto

        The model defined in huaweicloud sdk

        :param operator_id: 算子Id
        :type operator_id: str
        :param data_store_id: 存储ID
        :type data_store_id: str
        :param tag: 标签信息
        :type tag: str
        """
        
        

        self._operator_id = None
        self._data_store_id = None
        self._tag = None
        self.discriminator = None

        if operator_id is not None:
            self.operator_id = operator_id
        if data_store_id is not None:
            self.data_store_id = data_store_id
        if tag is not None:
            self.tag = tag

    @property
    def operator_id(self):
        """Gets the operator_id of this TagInfoDto.

        算子Id

        :return: The operator_id of this TagInfoDto.
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this TagInfoDto.

        算子Id

        :param operator_id: The operator_id of this TagInfoDto.
        :type operator_id: str
        """
        self._operator_id = operator_id

    @property
    def data_store_id(self):
        """Gets the data_store_id of this TagInfoDto.

        存储ID

        :return: The data_store_id of this TagInfoDto.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this TagInfoDto.

        存储ID

        :param data_store_id: The data_store_id of this TagInfoDto.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def tag(self):
        """Gets the tag of this TagInfoDto.

        标签信息

        :return: The tag of this TagInfoDto.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TagInfoDto.

        标签信息

        :param tag: The tag of this TagInfoDto.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, TagInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

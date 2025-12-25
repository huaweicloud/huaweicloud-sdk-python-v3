# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDictionaryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dict_list': 'list[DictionaryCreate]',
        'is_built_in': 'bool'
    }

    attribute_map = {
        'dict_list': 'dict_list',
        'is_built_in': 'is_built_in'
    }

    def __init__(self, dict_list=None, is_built_in=None):
        r"""CreateDictionaryRequest

        The model defined in huaweicloud sdk

        :param dict_list: 字典列表
        :type dict_list: list[:class:`huaweicloudsdksecmaster.v1.DictionaryCreate`]
        :param is_built_in: 是否创建内置字典
        :type is_built_in: bool
        """
        
        

        self._dict_list = None
        self._is_built_in = None
        self.discriminator = None

        if dict_list is not None:
            self.dict_list = dict_list
        if is_built_in is not None:
            self.is_built_in = is_built_in

    @property
    def dict_list(self):
        r"""Gets the dict_list of this CreateDictionaryRequest.

        字典列表

        :return: The dict_list of this CreateDictionaryRequest.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DictionaryCreate`]
        """
        return self._dict_list

    @dict_list.setter
    def dict_list(self, dict_list):
        r"""Sets the dict_list of this CreateDictionaryRequest.

        字典列表

        :param dict_list: The dict_list of this CreateDictionaryRequest.
        :type dict_list: list[:class:`huaweicloudsdksecmaster.v1.DictionaryCreate`]
        """
        self._dict_list = dict_list

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this CreateDictionaryRequest.

        是否创建内置字典

        :return: The is_built_in of this CreateDictionaryRequest.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this CreateDictionaryRequest.

        是否创建内置字典

        :param is_built_in: The is_built_in of this CreateDictionaryRequest.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

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
        if not isinstance(other, CreateDictionaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

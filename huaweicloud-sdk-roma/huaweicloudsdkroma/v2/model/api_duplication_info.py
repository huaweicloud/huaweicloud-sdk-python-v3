# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiDuplicationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'req_method': 'str',
        'req_uri': 'str',
        'match_mode': 'str',
        'duplicated_apis': 'list[DuplicateApiInfo]'
    }

    attribute_map = {
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'match_mode': 'match_mode',
        'duplicated_apis': 'duplicated_apis'
    }

    def __init__(self, req_method=None, req_uri=None, match_mode=None, duplicated_apis=None):
        """ApiDuplicationInfo

        The model defined in huaweicloud sdk

        :param req_method: 请求方式
        :type req_method: str
        :param req_uri: API的访问地址
        :type req_uri: str
        :param match_mode: API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL
        :type match_mode: str
        :param duplicated_apis: 该路径下冲突的api列表
        :type duplicated_apis: list[:class:`huaweicloudsdkroma.v2.DuplicateApiInfo`]
        """
        
        

        self._req_method = None
        self._req_uri = None
        self._match_mode = None
        self._duplicated_apis = None
        self.discriminator = None

        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri
        if match_mode is not None:
            self.match_mode = match_mode
        if duplicated_apis is not None:
            self.duplicated_apis = duplicated_apis

    @property
    def req_method(self):
        """Gets the req_method of this ApiDuplicationInfo.

        请求方式

        :return: The req_method of this ApiDuplicationInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ApiDuplicationInfo.

        请求方式

        :param req_method: The req_method of this ApiDuplicationInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ApiDuplicationInfo.

        API的访问地址

        :return: The req_uri of this ApiDuplicationInfo.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ApiDuplicationInfo.

        API的访问地址

        :param req_uri: The req_uri of this ApiDuplicationInfo.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def match_mode(self):
        """Gets the match_mode of this ApiDuplicationInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :return: The match_mode of this ApiDuplicationInfo.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this ApiDuplicationInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :param match_mode: The match_mode of this ApiDuplicationInfo.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def duplicated_apis(self):
        """Gets the duplicated_apis of this ApiDuplicationInfo.

        该路径下冲突的api列表

        :return: The duplicated_apis of this ApiDuplicationInfo.
        :rtype: list[:class:`huaweicloudsdkroma.v2.DuplicateApiInfo`]
        """
        return self._duplicated_apis

    @duplicated_apis.setter
    def duplicated_apis(self, duplicated_apis):
        """Sets the duplicated_apis of this ApiDuplicationInfo.

        该路径下冲突的api列表

        :param duplicated_apis: The duplicated_apis of this ApiDuplicationInfo.
        :type duplicated_apis: list[:class:`huaweicloudsdkroma.v2.DuplicateApiInfo`]
        """
        self._duplicated_apis = duplicated_apis

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
        if not isinstance(other, ApiDuplicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

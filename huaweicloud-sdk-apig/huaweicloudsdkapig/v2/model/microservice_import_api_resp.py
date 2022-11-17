# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroserviceImportApiResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'req_uri': 'str',
        'req_method': 'str',
        'id': 'str',
        'match_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'req_uri': 'req_uri',
        'req_method': 'req_method',
        'id': 'id',
        'match_mode': 'match_mode'
    }

    def __init__(self, name=None, req_uri=None, req_method=None, id=None, match_mode=None):
        """MicroserviceImportApiResp

        The model defined in huaweicloud sdk

        :param name: API名称
        :type name: str
        :param req_uri: API请求路径
        :type req_uri: str
        :param req_method: API请求方法
        :type req_method: str
        :param id: API编号
        :type id: str
        :param match_mode: API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：SWA
        :type match_mode: str
        """
        
        

        self._name = None
        self._req_uri = None
        self._req_method = None
        self._id = None
        self._match_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if req_uri is not None:
            self.req_uri = req_uri
        if req_method is not None:
            self.req_method = req_method
        if id is not None:
            self.id = id
        if match_mode is not None:
            self.match_mode = match_mode

    @property
    def name(self):
        """Gets the name of this MicroserviceImportApiResp.

        API名称

        :return: The name of this MicroserviceImportApiResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MicroserviceImportApiResp.

        API名称

        :param name: The name of this MicroserviceImportApiResp.
        :type name: str
        """
        self._name = name

    @property
    def req_uri(self):
        """Gets the req_uri of this MicroserviceImportApiResp.

        API请求路径

        :return: The req_uri of this MicroserviceImportApiResp.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this MicroserviceImportApiResp.

        API请求路径

        :param req_uri: The req_uri of this MicroserviceImportApiResp.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def req_method(self):
        """Gets the req_method of this MicroserviceImportApiResp.

        API请求方法

        :return: The req_method of this MicroserviceImportApiResp.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this MicroserviceImportApiResp.

        API请求方法

        :param req_method: The req_method of this MicroserviceImportApiResp.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def id(self):
        """Gets the id of this MicroserviceImportApiResp.

        API编号

        :return: The id of this MicroserviceImportApiResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MicroserviceImportApiResp.

        API编号

        :param id: The id of this MicroserviceImportApiResp.
        :type id: str
        """
        self._id = id

    @property
    def match_mode(self):
        """Gets the match_mode of this MicroserviceImportApiResp.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：SWA

        :return: The match_mode of this MicroserviceImportApiResp.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this MicroserviceImportApiResp.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：SWA

        :param match_mode: The match_mode of this MicroserviceImportApiResp.
        :type match_mode: str
        """
        self._match_mode = match_mode

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
        if not isinstance(other, MicroserviceImportApiResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

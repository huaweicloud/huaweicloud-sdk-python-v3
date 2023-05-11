# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiCheckInfo:

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
        'req_method': 'str',
        'req_uri': 'str',
        'match_mode': 'str',
        'group_id': 'str',
        'roma_app_id': 'str',
        'api_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'match_mode': 'match_mode',
        'group_id': 'group_id',
        'roma_app_id': 'roma_app_id',
        'api_id': 'api_id'
    }

    def __init__(self, name=None, req_method=None, req_uri=None, match_mode=None, group_id=None, roma_app_id=None, api_id=None):
        """ApiCheckInfo

        The model defined in huaweicloud sdk

        :param name: API名称。  type &#x3D; name时必填
        :type name: str
        :param req_method: 请求方式。  type &#x3D; path时必填
        :type req_method: str
        :param req_uri: API的访问地址。  type &#x3D; path时必填
        :type req_uri: str
        :param match_mode: API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）  type &#x3D; path时必填
        :type match_mode: str
        :param group_id: 分组ID。  校验分组下API定义是否重复时必填
        :type group_id: str
        :param roma_app_id: 集成应用ID。  校验应用下API定义是否重复时必填
        :type roma_app_id: str
        :param api_id: 需要对比的API ID
        :type api_id: str
        """
        
        

        self._name = None
        self._req_method = None
        self._req_uri = None
        self._match_mode = None
        self._group_id = None
        self._roma_app_id = None
        self._api_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri
        if match_mode is not None:
            self.match_mode = match_mode
        if group_id is not None:
            self.group_id = group_id
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if api_id is not None:
            self.api_id = api_id

    @property
    def name(self):
        """Gets the name of this ApiCheckInfo.

        API名称。  type = name时必填

        :return: The name of this ApiCheckInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCheckInfo.

        API名称。  type = name时必填

        :param name: The name of this ApiCheckInfo.
        :type name: str
        """
        self._name = name

    @property
    def req_method(self):
        """Gets the req_method of this ApiCheckInfo.

        请求方式。  type = path时必填

        :return: The req_method of this ApiCheckInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ApiCheckInfo.

        请求方式。  type = path时必填

        :param req_method: The req_method of this ApiCheckInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ApiCheckInfo.

        API的访问地址。  type = path时必填

        :return: The req_uri of this ApiCheckInfo.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ApiCheckInfo.

        API的访问地址。  type = path时必填

        :param req_uri: The req_uri of this ApiCheckInfo.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def match_mode(self):
        """Gets the match_mode of this ApiCheckInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）  type = path时必填

        :return: The match_mode of this ApiCheckInfo.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this ApiCheckInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）  type = path时必填

        :param match_mode: The match_mode of this ApiCheckInfo.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def group_id(self):
        """Gets the group_id of this ApiCheckInfo.

        分组ID。  校验分组下API定义是否重复时必填

        :return: The group_id of this ApiCheckInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ApiCheckInfo.

        分组ID。  校验分组下API定义是否重复时必填

        :param group_id: The group_id of this ApiCheckInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this ApiCheckInfo.

        集成应用ID。  校验应用下API定义是否重复时必填

        :return: The roma_app_id of this ApiCheckInfo.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this ApiCheckInfo.

        集成应用ID。  校验应用下API定义是否重复时必填

        :param roma_app_id: The roma_app_id of this ApiCheckInfo.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def api_id(self):
        """Gets the api_id of this ApiCheckInfo.

        需要对比的API ID

        :return: The api_id of this ApiCheckInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ApiCheckInfo.

        需要对比的API ID

        :param api_id: The api_id of this ApiCheckInfo.
        :type api_id: str
        """
        self._api_id = api_id

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
        if not isinstance(other, ApiCheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

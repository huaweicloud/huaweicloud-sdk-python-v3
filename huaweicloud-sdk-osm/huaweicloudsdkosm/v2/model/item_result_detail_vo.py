# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemResultDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'level': 'int',
        'suggestion': 'str',
        'response': 'str',
        'check_id': 'str',
        'check_name': 'str',
        'check_name_en': 'str',
        'suggestion_url': 'str'
    }

    attribute_map = {
        'status': 'status',
        'level': 'level',
        'suggestion': 'suggestion',
        'response': 'response',
        'check_id': 'check_id',
        'check_name': 'check_name',
        'check_name_en': 'check_name_en',
        'suggestion_url': 'suggestion_url'
    }

    def __init__(self, status=None, level=None, suggestion=None, response=None, check_id=None, check_name=None, check_name_en=None, suggestion_url=None):
        """ItemResultDetailVo

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: int
        :param level: 检查项风险等级
        :type level: int
        :param suggestion: 检查项修复建议
        :type suggestion: str
        :param response: 检查项response
        :type response: str
        :param check_id: 检查项ID
        :type check_id: str
        :param check_name: 检查项名称
        :type check_name: str
        :param check_name_en: 检查项英文名称
        :type check_name_en: str
        :param suggestion_url: 检查项修复建议URL
        :type suggestion_url: str
        """
        
        

        self._status = None
        self._level = None
        self._suggestion = None
        self._response = None
        self._check_id = None
        self._check_name = None
        self._check_name_en = None
        self._suggestion_url = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if level is not None:
            self.level = level
        if suggestion is not None:
            self.suggestion = suggestion
        if response is not None:
            self.response = response
        if check_id is not None:
            self.check_id = check_id
        if check_name is not None:
            self.check_name = check_name
        if check_name_en is not None:
            self.check_name_en = check_name_en
        if suggestion_url is not None:
            self.suggestion_url = suggestion_url

    @property
    def status(self):
        """Gets the status of this ItemResultDetailVo.

        状态

        :return: The status of this ItemResultDetailVo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemResultDetailVo.

        状态

        :param status: The status of this ItemResultDetailVo.
        :type status: int
        """
        self._status = status

    @property
    def level(self):
        """Gets the level of this ItemResultDetailVo.

        检查项风险等级

        :return: The level of this ItemResultDetailVo.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ItemResultDetailVo.

        检查项风险等级

        :param level: The level of this ItemResultDetailVo.
        :type level: int
        """
        self._level = level

    @property
    def suggestion(self):
        """Gets the suggestion of this ItemResultDetailVo.

        检查项修复建议

        :return: The suggestion of this ItemResultDetailVo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ItemResultDetailVo.

        检查项修复建议

        :param suggestion: The suggestion of this ItemResultDetailVo.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def response(self):
        """Gets the response of this ItemResultDetailVo.

        检查项response

        :return: The response of this ItemResultDetailVo.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ItemResultDetailVo.

        检查项response

        :param response: The response of this ItemResultDetailVo.
        :type response: str
        """
        self._response = response

    @property
    def check_id(self):
        """Gets the check_id of this ItemResultDetailVo.

        检查项ID

        :return: The check_id of this ItemResultDetailVo.
        :rtype: str
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this ItemResultDetailVo.

        检查项ID

        :param check_id: The check_id of this ItemResultDetailVo.
        :type check_id: str
        """
        self._check_id = check_id

    @property
    def check_name(self):
        """Gets the check_name of this ItemResultDetailVo.

        检查项名称

        :return: The check_name of this ItemResultDetailVo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        """Sets the check_name of this ItemResultDetailVo.

        检查项名称

        :param check_name: The check_name of this ItemResultDetailVo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_name_en(self):
        """Gets the check_name_en of this ItemResultDetailVo.

        检查项英文名称

        :return: The check_name_en of this ItemResultDetailVo.
        :rtype: str
        """
        return self._check_name_en

    @check_name_en.setter
    def check_name_en(self, check_name_en):
        """Sets the check_name_en of this ItemResultDetailVo.

        检查项英文名称

        :param check_name_en: The check_name_en of this ItemResultDetailVo.
        :type check_name_en: str
        """
        self._check_name_en = check_name_en

    @property
    def suggestion_url(self):
        """Gets the suggestion_url of this ItemResultDetailVo.

        检查项修复建议URL

        :return: The suggestion_url of this ItemResultDetailVo.
        :rtype: str
        """
        return self._suggestion_url

    @suggestion_url.setter
    def suggestion_url(self, suggestion_url):
        """Sets the suggestion_url of this ItemResultDetailVo.

        检查项修复建议URL

        :param suggestion_url: The suggestion_url of this ItemResultDetailVo.
        :type suggestion_url: str
        """
        self._suggestion_url = suggestion_url

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
        if not isinstance(other, ItemResultDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

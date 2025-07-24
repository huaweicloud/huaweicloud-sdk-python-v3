# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'status': 'str',
        'name_cn': 'str',
        'name_en': 'str',
        'effect_cn': 'str',
        'effect_en': 'str',
        'suggestion_cn': 'str',
        'suggestion_en': 'str',
        'reason_cn': 'str',
        'reason_en': 'str'
    }

    attribute_map = {
        'code': 'code',
        'status': 'status',
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'effect_cn': 'effect_cn',
        'effect_en': 'effect_en',
        'suggestion_cn': 'suggestion_cn',
        'suggestion_en': 'suggestion_en',
        'reason_cn': 'reason_cn',
        'reason_en': 'reason_en'
    }

    def __init__(self, code=None, status=None, name_cn=None, name_en=None, effect_cn=None, effect_en=None, suggestion_cn=None, suggestion_en=None, reason_cn=None, reason_en=None):
        r"""ShowEventResponse

        The model defined in huaweicloud sdk

        :param code: 事件码
        :type code: str
        :param status: 状态
        :type status: str
        :param name_cn: 事件中文名称
        :type name_cn: str
        :param name_en: 事件英文名称
        :type name_en: str
        :param effect_cn: 事件中文影响
        :type effect_cn: str
        :param effect_en: 事件英文影响
        :type effect_en: str
        :param suggestion_cn: 事件中文处理建议
        :type suggestion_cn: str
        :param suggestion_en: 事件英文处理建议
        :type suggestion_en: str
        :param reason_cn: 事件中文原因
        :type reason_cn: str
        :param reason_en: 事件英文原因
        :type reason_en: str
        """
        
        super(ShowEventResponse, self).__init__()

        self._code = None
        self._status = None
        self._name_cn = None
        self._name_en = None
        self._effect_cn = None
        self._effect_en = None
        self._suggestion_cn = None
        self._suggestion_en = None
        self._reason_cn = None
        self._reason_en = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if name_cn is not None:
            self.name_cn = name_cn
        if name_en is not None:
            self.name_en = name_en
        if effect_cn is not None:
            self.effect_cn = effect_cn
        if effect_en is not None:
            self.effect_en = effect_en
        if suggestion_cn is not None:
            self.suggestion_cn = suggestion_cn
        if suggestion_en is not None:
            self.suggestion_en = suggestion_en
        if reason_cn is not None:
            self.reason_cn = reason_cn
        if reason_en is not None:
            self.reason_en = reason_en

    @property
    def code(self):
        r"""Gets the code of this ShowEventResponse.

        事件码

        :return: The code of this ShowEventResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowEventResponse.

        事件码

        :param code: The code of this ShowEventResponse.
        :type code: str
        """
        self._code = code

    @property
    def status(self):
        r"""Gets the status of this ShowEventResponse.

        状态

        :return: The status of this ShowEventResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowEventResponse.

        状态

        :param status: The status of this ShowEventResponse.
        :type status: str
        """
        self._status = status

    @property
    def name_cn(self):
        r"""Gets the name_cn of this ShowEventResponse.

        事件中文名称

        :return: The name_cn of this ShowEventResponse.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this ShowEventResponse.

        事件中文名称

        :param name_cn: The name_cn of this ShowEventResponse.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this ShowEventResponse.

        事件英文名称

        :return: The name_en of this ShowEventResponse.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this ShowEventResponse.

        事件英文名称

        :param name_en: The name_en of this ShowEventResponse.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def effect_cn(self):
        r"""Gets the effect_cn of this ShowEventResponse.

        事件中文影响

        :return: The effect_cn of this ShowEventResponse.
        :rtype: str
        """
        return self._effect_cn

    @effect_cn.setter
    def effect_cn(self, effect_cn):
        r"""Sets the effect_cn of this ShowEventResponse.

        事件中文影响

        :param effect_cn: The effect_cn of this ShowEventResponse.
        :type effect_cn: str
        """
        self._effect_cn = effect_cn

    @property
    def effect_en(self):
        r"""Gets the effect_en of this ShowEventResponse.

        事件英文影响

        :return: The effect_en of this ShowEventResponse.
        :rtype: str
        """
        return self._effect_en

    @effect_en.setter
    def effect_en(self, effect_en):
        r"""Sets the effect_en of this ShowEventResponse.

        事件英文影响

        :param effect_en: The effect_en of this ShowEventResponse.
        :type effect_en: str
        """
        self._effect_en = effect_en

    @property
    def suggestion_cn(self):
        r"""Gets the suggestion_cn of this ShowEventResponse.

        事件中文处理建议

        :return: The suggestion_cn of this ShowEventResponse.
        :rtype: str
        """
        return self._suggestion_cn

    @suggestion_cn.setter
    def suggestion_cn(self, suggestion_cn):
        r"""Sets the suggestion_cn of this ShowEventResponse.

        事件中文处理建议

        :param suggestion_cn: The suggestion_cn of this ShowEventResponse.
        :type suggestion_cn: str
        """
        self._suggestion_cn = suggestion_cn

    @property
    def suggestion_en(self):
        r"""Gets the suggestion_en of this ShowEventResponse.

        事件英文处理建议

        :return: The suggestion_en of this ShowEventResponse.
        :rtype: str
        """
        return self._suggestion_en

    @suggestion_en.setter
    def suggestion_en(self, suggestion_en):
        r"""Sets the suggestion_en of this ShowEventResponse.

        事件英文处理建议

        :param suggestion_en: The suggestion_en of this ShowEventResponse.
        :type suggestion_en: str
        """
        self._suggestion_en = suggestion_en

    @property
    def reason_cn(self):
        r"""Gets the reason_cn of this ShowEventResponse.

        事件中文原因

        :return: The reason_cn of this ShowEventResponse.
        :rtype: str
        """
        return self._reason_cn

    @reason_cn.setter
    def reason_cn(self, reason_cn):
        r"""Sets the reason_cn of this ShowEventResponse.

        事件中文原因

        :param reason_cn: The reason_cn of this ShowEventResponse.
        :type reason_cn: str
        """
        self._reason_cn = reason_cn

    @property
    def reason_en(self):
        r"""Gets the reason_en of this ShowEventResponse.

        事件英文原因

        :return: The reason_en of this ShowEventResponse.
        :rtype: str
        """
        return self._reason_en

    @reason_en.setter
    def reason_en(self, reason_en):
        r"""Sets the reason_en of this ShowEventResponse.

        事件英文原因

        :param reason_en: The reason_en of this ShowEventResponse.
        :type reason_en: str
        """
        self._reason_en = reason_en

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
        if not isinstance(other, ShowEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

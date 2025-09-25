# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'version': 'str',
        'duration': 'str',
        'domain_id': 'str',
        'is_valid': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'duration': 'duration',
        'domain_id': 'domain_id',
        'is_valid': 'is_valid'
    }

    def __init__(self, id=None, name=None, version=None, duration=None, domain_id=None, is_valid=None):
        r"""CheckAgencyResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 代理id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param name: **参数解释：** 代理名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param version: **参数解释：** 版本 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type version: str
        :param duration: **参数解释：** 代理存在时间段 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type duration: str
        :param domain_id: **参数解释：** 使用代理的domainid **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_id: str
        :param is_valid: **参数解释：** 代理是否合法 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type is_valid: bool
        """
        
        super(CheckAgencyResponse, self).__init__()

        self._id = None
        self._name = None
        self._version = None
        self._duration = None
        self._domain_id = None
        self._is_valid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if duration is not None:
            self.duration = duration
        if domain_id is not None:
            self.domain_id = domain_id
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def id(self):
        r"""Gets the id of this CheckAgencyResponse.

        **参数解释：** 代理id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this CheckAgencyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CheckAgencyResponse.

        **参数解释：** 代理id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this CheckAgencyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CheckAgencyResponse.

        **参数解释：** 代理名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this CheckAgencyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckAgencyResponse.

        **参数解释：** 代理名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this CheckAgencyResponse.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this CheckAgencyResponse.

        **参数解释：** 版本 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The version of this CheckAgencyResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CheckAgencyResponse.

        **参数解释：** 版本 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param version: The version of this CheckAgencyResponse.
        :type version: str
        """
        self._version = version

    @property
    def duration(self):
        r"""Gets the duration of this CheckAgencyResponse.

        **参数解释：** 代理存在时间段 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The duration of this CheckAgencyResponse.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this CheckAgencyResponse.

        **参数解释：** 代理存在时间段 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param duration: The duration of this CheckAgencyResponse.
        :type duration: str
        """
        self._duration = duration

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CheckAgencyResponse.

        **参数解释：** 使用代理的domainid **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_id of this CheckAgencyResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CheckAgencyResponse.

        **参数解释：** 使用代理的domainid **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_id: The domain_id of this CheckAgencyResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def is_valid(self):
        r"""Gets the is_valid of this CheckAgencyResponse.

        **参数解释：** 代理是否合法 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The is_valid of this CheckAgencyResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this CheckAgencyResponse.

        **参数解释：** 代理是否合法 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param is_valid: The is_valid of this CheckAgencyResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

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
        if not isinstance(other, CheckAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

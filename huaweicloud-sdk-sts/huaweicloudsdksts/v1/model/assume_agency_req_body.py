# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration_seconds': 'int',
        'external_id': 'str',
        'policy': 'str',
        'policy_ids': 'list[str]',
        'agency_urn': 'str',
        'agency_session_name': 'str',
        'serial_number': 'str',
        'token_code': 'str',
        'source_identity': 'str',
        'tags': 'list[TagDto]',
        'transitive_tag_keys': 'list[str]'
    }

    attribute_map = {
        'duration_seconds': 'duration_seconds',
        'external_id': 'external_id',
        'policy': 'policy',
        'policy_ids': 'policy_ids',
        'agency_urn': 'agency_urn',
        'agency_session_name': 'agency_session_name',
        'serial_number': 'serial_number',
        'token_code': 'token_code',
        'source_identity': 'source_identity',
        'tags': 'tags',
        'transitive_tag_keys': 'transitive_tag_keys'
    }

    def __init__(self, duration_seconds=None, external_id=None, policy=None, policy_ids=None, agency_urn=None, agency_session_name=None, serial_number=None, token_code=None, source_identity=None, tags=None, transitive_tag_keys=None):
        r"""AssumeAgencyReqBody

        The model defined in huaweicloud sdk

        :param duration_seconds: 获得的临时安全凭证的有效时间（单位秒）。请注意，该时间需要小于委托本身设置的最大会话持续时间，同时在携带X-Security-Token的Header头时该时间不能超过3600秒。
        :type duration_seconds: int
        :param external_id: 外部ID，防止混淆代理人问题。
        :type external_id: str
        :param policy: 自定义策略，限制本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。
        :type policy: str
        :param policy_ids: 预置策略列表，限制本次会话获得的临时安全凭证的权限范围不会超过该预置策略指定的权限。
        :type policy_ids: list[str]
        :param agency_urn: 目标委托的URN。
        :type agency_urn: str
        :param agency_session_name: 委托会话的会话名。
        :type agency_session_name: str
        :param serial_number: 调用者绑定的MFA设备的序列号。
        :type serial_number: str
        :param token_code: 调用者绑定的MFA设备上的6位数字码。
        :type token_code: str
        :param source_identity: 调用链里最初调用者所声明的身份。
        :type source_identity: str
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdksts.v1.TagDto`]
        :param transitive_tag_keys: 随着临时安全凭证调用链持续透传的标签键列表。
        :type transitive_tag_keys: list[str]
        """
        
        

        self._duration_seconds = None
        self._external_id = None
        self._policy = None
        self._policy_ids = None
        self._agency_urn = None
        self._agency_session_name = None
        self._serial_number = None
        self._token_code = None
        self._source_identity = None
        self._tags = None
        self._transitive_tag_keys = None
        self.discriminator = None

        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        if external_id is not None:
            self.external_id = external_id
        if policy is not None:
            self.policy = policy
        if policy_ids is not None:
            self.policy_ids = policy_ids
        self.agency_urn = agency_urn
        self.agency_session_name = agency_session_name
        if serial_number is not None:
            self.serial_number = serial_number
        if token_code is not None:
            self.token_code = token_code
        if source_identity is not None:
            self.source_identity = source_identity
        if tags is not None:
            self.tags = tags
        if transitive_tag_keys is not None:
            self.transitive_tag_keys = transitive_tag_keys

    @property
    def duration_seconds(self):
        r"""Gets the duration_seconds of this AssumeAgencyReqBody.

        获得的临时安全凭证的有效时间（单位秒）。请注意，该时间需要小于委托本身设置的最大会话持续时间，同时在携带X-Security-Token的Header头时该时间不能超过3600秒。

        :return: The duration_seconds of this AssumeAgencyReqBody.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        r"""Sets the duration_seconds of this AssumeAgencyReqBody.

        获得的临时安全凭证的有效时间（单位秒）。请注意，该时间需要小于委托本身设置的最大会话持续时间，同时在携带X-Security-Token的Header头时该时间不能超过3600秒。

        :param duration_seconds: The duration_seconds of this AssumeAgencyReqBody.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

    @property
    def external_id(self):
        r"""Gets the external_id of this AssumeAgencyReqBody.

        外部ID，防止混淆代理人问题。

        :return: The external_id of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this AssumeAgencyReqBody.

        外部ID，防止混淆代理人问题。

        :param external_id: The external_id of this AssumeAgencyReqBody.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def policy(self):
        r"""Gets the policy of this AssumeAgencyReqBody.

        自定义策略，限制本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。

        :return: The policy of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this AssumeAgencyReqBody.

        自定义策略，限制本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。

        :param policy: The policy of this AssumeAgencyReqBody.
        :type policy: str
        """
        self._policy = policy

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this AssumeAgencyReqBody.

        预置策略列表，限制本次会话获得的临时安全凭证的权限范围不会超过该预置策略指定的权限。

        :return: The policy_ids of this AssumeAgencyReqBody.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this AssumeAgencyReqBody.

        预置策略列表，限制本次会话获得的临时安全凭证的权限范围不会超过该预置策略指定的权限。

        :param policy_ids: The policy_ids of this AssumeAgencyReqBody.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

    @property
    def agency_urn(self):
        r"""Gets the agency_urn of this AssumeAgencyReqBody.

        目标委托的URN。

        :return: The agency_urn of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._agency_urn

    @agency_urn.setter
    def agency_urn(self, agency_urn):
        r"""Sets the agency_urn of this AssumeAgencyReqBody.

        目标委托的URN。

        :param agency_urn: The agency_urn of this AssumeAgencyReqBody.
        :type agency_urn: str
        """
        self._agency_urn = agency_urn

    @property
    def agency_session_name(self):
        r"""Gets the agency_session_name of this AssumeAgencyReqBody.

        委托会话的会话名。

        :return: The agency_session_name of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._agency_session_name

    @agency_session_name.setter
    def agency_session_name(self, agency_session_name):
        r"""Sets the agency_session_name of this AssumeAgencyReqBody.

        委托会话的会话名。

        :param agency_session_name: The agency_session_name of this AssumeAgencyReqBody.
        :type agency_session_name: str
        """
        self._agency_session_name = agency_session_name

    @property
    def serial_number(self):
        r"""Gets the serial_number of this AssumeAgencyReqBody.

        调用者绑定的MFA设备的序列号。

        :return: The serial_number of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this AssumeAgencyReqBody.

        调用者绑定的MFA设备的序列号。

        :param serial_number: The serial_number of this AssumeAgencyReqBody.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def token_code(self):
        r"""Gets the token_code of this AssumeAgencyReqBody.

        调用者绑定的MFA设备上的6位数字码。

        :return: The token_code of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._token_code

    @token_code.setter
    def token_code(self, token_code):
        r"""Sets the token_code of this AssumeAgencyReqBody.

        调用者绑定的MFA设备上的6位数字码。

        :param token_code: The token_code of this AssumeAgencyReqBody.
        :type token_code: str
        """
        self._token_code = token_code

    @property
    def source_identity(self):
        r"""Gets the source_identity of this AssumeAgencyReqBody.

        调用链里最初调用者所声明的身份。

        :return: The source_identity of this AssumeAgencyReqBody.
        :rtype: str
        """
        return self._source_identity

    @source_identity.setter
    def source_identity(self, source_identity):
        r"""Sets the source_identity of this AssumeAgencyReqBody.

        调用链里最初调用者所声明的身份。

        :param source_identity: The source_identity of this AssumeAgencyReqBody.
        :type source_identity: str
        """
        self._source_identity = source_identity

    @property
    def tags(self):
        r"""Gets the tags of this AssumeAgencyReqBody.

        自定义标签列表。

        :return: The tags of this AssumeAgencyReqBody.
        :rtype: list[:class:`huaweicloudsdksts.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this AssumeAgencyReqBody.

        自定义标签列表。

        :param tags: The tags of this AssumeAgencyReqBody.
        :type tags: list[:class:`huaweicloudsdksts.v1.TagDto`]
        """
        self._tags = tags

    @property
    def transitive_tag_keys(self):
        r"""Gets the transitive_tag_keys of this AssumeAgencyReqBody.

        随着临时安全凭证调用链持续透传的标签键列表。

        :return: The transitive_tag_keys of this AssumeAgencyReqBody.
        :rtype: list[str]
        """
        return self._transitive_tag_keys

    @transitive_tag_keys.setter
    def transitive_tag_keys(self, transitive_tag_keys):
        r"""Sets the transitive_tag_keys of this AssumeAgencyReqBody.

        随着临时安全凭证调用链持续透传的标签键列表。

        :param transitive_tag_keys: The transitive_tag_keys of this AssumeAgencyReqBody.
        :type transitive_tag_keys: list[str]
        """
        self._transitive_tag_keys = transitive_tag_keys

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
        if not isinstance(other, AssumeAgencyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

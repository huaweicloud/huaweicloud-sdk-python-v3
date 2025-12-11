# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'ServerState',
        'ok': 'ServerState',
        'warning': 'ServerState',
        'unknown': 'ServerState',
        'critical': 'ServerState',
        'health': 'ServerState',
        'unhealth': 'ServerState',
        'isolation': 'ServerState'
    }

    attribute_map = {
        'total': 'total',
        'ok': 'ok',
        'warning': 'warning',
        'unknown': 'unknown',
        'critical': 'critical',
        'health': 'health',
        'unhealth': 'unhealth',
        'isolation': 'isolation'
    }

    def __init__(self, total=None, ok=None, warning=None, unknown=None, critical=None, health=None, unhealth=None, isolation=None):
        r"""ServerStatus

        The model defined in huaweicloud sdk

        :param total: 
        :type total: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param ok: 
        :type ok: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param warning: 
        :type warning: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param unknown: 
        :type unknown: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param critical: 
        :type critical: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param health: 
        :type health: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param unhealth: 
        :type unhealth: :class:`huaweicloudsdkclouddc.v1.ServerState`
        :param isolation: 
        :type isolation: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        
        

        self._total = None
        self._ok = None
        self._warning = None
        self._unknown = None
        self._critical = None
        self._health = None
        self._unhealth = None
        self._isolation = None
        self.discriminator = None

        self.total = total
        self.ok = ok
        self.warning = warning
        if unknown is not None:
            self.unknown = unknown
        self.critical = critical
        self.health = health
        if unhealth is not None:
            self.unhealth = unhealth
        self.isolation = isolation

    @property
    def total(self):
        r"""Gets the total of this ServerStatus.

        :return: The total of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ServerStatus.

        :param total: The total of this ServerStatus.
        :type total: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._total = total

    @property
    def ok(self):
        r"""Gets the ok of this ServerStatus.

        :return: The ok of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        r"""Sets the ok of this ServerStatus.

        :param ok: The ok of this ServerStatus.
        :type ok: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._ok = ok

    @property
    def warning(self):
        r"""Gets the warning of this ServerStatus.

        :return: The warning of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        r"""Sets the warning of this ServerStatus.

        :param warning: The warning of this ServerStatus.
        :type warning: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._warning = warning

    @property
    def unknown(self):
        r"""Gets the unknown of this ServerStatus.

        :return: The unknown of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        r"""Sets the unknown of this ServerStatus.

        :param unknown: The unknown of this ServerStatus.
        :type unknown: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._unknown = unknown

    @property
    def critical(self):
        r"""Gets the critical of this ServerStatus.

        :return: The critical of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        r"""Sets the critical of this ServerStatus.

        :param critical: The critical of this ServerStatus.
        :type critical: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._critical = critical

    @property
    def health(self):
        r"""Gets the health of this ServerStatus.

        :return: The health of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this ServerStatus.

        :param health: The health of this ServerStatus.
        :type health: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._health = health

    @property
    def unhealth(self):
        r"""Gets the unhealth of this ServerStatus.

        :return: The unhealth of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._unhealth

    @unhealth.setter
    def unhealth(self, unhealth):
        r"""Sets the unhealth of this ServerStatus.

        :param unhealth: The unhealth of this ServerStatus.
        :type unhealth: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._unhealth = unhealth

    @property
    def isolation(self):
        r"""Gets the isolation of this ServerStatus.

        :return: The isolation of this ServerStatus.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        return self._isolation

    @isolation.setter
    def isolation(self, isolation):
        r"""Sets the isolation of this ServerStatus.

        :param isolation: The isolation of this ServerStatus.
        :type isolation: :class:`huaweicloudsdkclouddc.v1.ServerState`
        """
        self._isolation = isolation

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
        if not isinstance(other, ServerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

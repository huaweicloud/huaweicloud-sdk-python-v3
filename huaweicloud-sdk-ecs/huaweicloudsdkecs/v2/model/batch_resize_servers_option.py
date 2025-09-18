# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResizeServersOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'servers': 'list[ServerId]',
        'cpu_options': 'CpuOptions',
        'mode': 'str',
        'promotion': 'Promotion'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'servers': 'servers',
        'cpu_options': 'cpu_options',
        'mode': 'mode',
        'promotion': 'promotion'
    }

    def __init__(self, flavor_ref=None, servers=None, cpu_options=None, mode=None, promotion=None):
        r"""BatchResizeServersOption

        The model defined in huaweicloud sdk

        :param flavor_ref: flavor
        :type flavor_ref: str
        :param servers: 
        :type servers: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        :param cpu_options: 
        :type cpu_options: :class:`huaweicloudsdkecs.v2.CpuOptions`
        :param mode: 
        :type mode: str
        :param promotion: 
        :type promotion: :class:`huaweicloudsdkecs.v2.Promotion`
        """
        
        

        self._flavor_ref = None
        self._servers = None
        self._cpu_options = None
        self._mode = None
        self._promotion = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.servers = servers
        if cpu_options is not None:
            self.cpu_options = cpu_options
        if mode is not None:
            self.mode = mode
        if promotion is not None:
            self.promotion = promotion

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this BatchResizeServersOption.

        flavor

        :return: The flavor_ref of this BatchResizeServersOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this BatchResizeServersOption.

        flavor

        :param flavor_ref: The flavor_ref of this BatchResizeServersOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def servers(self):
        r"""Gets the servers of this BatchResizeServersOption.

        :return: The servers of this BatchResizeServersOption.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this BatchResizeServersOption.

        :param servers: The servers of this BatchResizeServersOption.
        :type servers: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        self._servers = servers

    @property
    def cpu_options(self):
        r"""Gets the cpu_options of this BatchResizeServersOption.

        :return: The cpu_options of this BatchResizeServersOption.
        :rtype: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        return self._cpu_options

    @cpu_options.setter
    def cpu_options(self, cpu_options):
        r"""Sets the cpu_options of this BatchResizeServersOption.

        :param cpu_options: The cpu_options of this BatchResizeServersOption.
        :type cpu_options: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        self._cpu_options = cpu_options

    @property
    def mode(self):
        r"""Gets the mode of this BatchResizeServersOption.

        :return: The mode of this BatchResizeServersOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this BatchResizeServersOption.

        :param mode: The mode of this BatchResizeServersOption.
        :type mode: str
        """
        self._mode = mode

    @property
    def promotion(self):
        r"""Gets the promotion of this BatchResizeServersOption.

        :return: The promotion of this BatchResizeServersOption.
        :rtype: :class:`huaweicloudsdkecs.v2.Promotion`
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        r"""Sets the promotion of this BatchResizeServersOption.

        :param promotion: The promotion of this BatchResizeServersOption.
        :type promotion: :class:`huaweicloudsdkecs.v2.Promotion`
        """
        self._promotion = promotion

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
        if not isinstance(other, BatchResizeServersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

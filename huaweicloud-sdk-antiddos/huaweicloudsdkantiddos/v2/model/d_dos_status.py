# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DDosStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'floating_ip_id': 'str',
        'floating_ip_address': 'str',
        'product_type': 'str',
        'status': 'str',
        'clean_threshold': 'int',
        'block_threshold': 'str'
    }

    attribute_map = {
        'floating_ip_id': 'floating_ip_id',
        'floating_ip_address': 'floating_ip_address',
        'product_type': 'product_type',
        'status': 'status',
        'clean_threshold': 'clean_threshold',
        'block_threshold': 'block_threshold'
    }

    def __init__(self, floating_ip_id=None, floating_ip_address=None, product_type=None, status=None, clean_threshold=None, block_threshold=None):
        r"""DDosStatus

        The model defined in huaweicloud sdk

        :param floating_ip_id: EIP的ID
        :type floating_ip_id: str
        :param floating_ip_address: 浮动IP地址
        :type floating_ip_address: str
        :param product_type: EIP所属类型，可选范围： - Anti-DDoS：eip属于Anti-DDoS流量清洗 - CNAD：eip属于DDoS原生高级防护
        :type product_type: str
        :param status: 防护状态，可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞
        :type status: str
        :param clean_threshold: 清洗阈值
        :type clean_threshold: int
        :param block_threshold: 黑洞阈值
        :type block_threshold: str
        """
        
        

        self._floating_ip_id = None
        self._floating_ip_address = None
        self._product_type = None
        self._status = None
        self._clean_threshold = None
        self._block_threshold = None
        self.discriminator = None

        self.floating_ip_id = floating_ip_id
        self.floating_ip_address = floating_ip_address
        self.product_type = product_type
        self.status = status
        self.clean_threshold = clean_threshold
        self.block_threshold = block_threshold

    @property
    def floating_ip_id(self):
        r"""Gets the floating_ip_id of this DDosStatus.

        EIP的ID

        :return: The floating_ip_id of this DDosStatus.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        r"""Sets the floating_ip_id of this DDosStatus.

        EIP的ID

        :param floating_ip_id: The floating_ip_id of this DDosStatus.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def floating_ip_address(self):
        r"""Gets the floating_ip_address of this DDosStatus.

        浮动IP地址

        :return: The floating_ip_address of this DDosStatus.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        r"""Sets the floating_ip_address of this DDosStatus.

        浮动IP地址

        :param floating_ip_address: The floating_ip_address of this DDosStatus.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def product_type(self):
        r"""Gets the product_type of this DDosStatus.

        EIP所属类型，可选范围： - Anti-DDoS：eip属于Anti-DDoS流量清洗 - CNAD：eip属于DDoS原生高级防护

        :return: The product_type of this DDosStatus.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this DDosStatus.

        EIP所属类型，可选范围： - Anti-DDoS：eip属于Anti-DDoS流量清洗 - CNAD：eip属于DDoS原生高级防护

        :param product_type: The product_type of this DDosStatus.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def status(self):
        r"""Gets the status of this DDosStatus.

        防护状态，可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞

        :return: The status of this DDosStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DDosStatus.

        防护状态，可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞

        :param status: The status of this DDosStatus.
        :type status: str
        """
        self._status = status

    @property
    def clean_threshold(self):
        r"""Gets the clean_threshold of this DDosStatus.

        清洗阈值

        :return: The clean_threshold of this DDosStatus.
        :rtype: int
        """
        return self._clean_threshold

    @clean_threshold.setter
    def clean_threshold(self, clean_threshold):
        r"""Sets the clean_threshold of this DDosStatus.

        清洗阈值

        :param clean_threshold: The clean_threshold of this DDosStatus.
        :type clean_threshold: int
        """
        self._clean_threshold = clean_threshold

    @property
    def block_threshold(self):
        r"""Gets the block_threshold of this DDosStatus.

        黑洞阈值

        :return: The block_threshold of this DDosStatus.
        :rtype: str
        """
        return self._block_threshold

    @block_threshold.setter
    def block_threshold(self, block_threshold):
        r"""Sets the block_threshold of this DDosStatus.

        黑洞阈值

        :param block_threshold: The block_threshold of this DDosStatus.
        :type block_threshold: str
        """
        self._block_threshold = block_threshold

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
        if not isinstance(other, DDosStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

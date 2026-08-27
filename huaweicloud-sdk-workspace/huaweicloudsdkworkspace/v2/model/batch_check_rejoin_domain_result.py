# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCheckRejoinDomainResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'desktop_name': 'str',
        'image_name': 'str',
        'domain_status': 'int',
        'rejoin_able': 'bool',
        'product': 'ProductInfo',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'image_name': 'image_name',
        'domain_status': 'domain_status',
        'rejoin_able': 'rejoin_able',
        'product': 'product',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, desktop_id=None, desktop_name=None, image_name=None, domain_status=None, rejoin_able=None, product=None, error_code=None, error_msg=None):
        r"""BatchCheckRejoinDomainResult

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param image_name: 镜像名称。
        :type image_name: str
        :param domain_status: 加域状态。|- 1 正常。 2 脱域。 3 未上报。
        :type domain_status: int
        :param rejoin_able: 是否可以加域。
        :type rejoin_able: bool
        :param product: 
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._image_name = None
        self._domain_status = None
        self._rejoin_able = None
        self._product = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if image_name is not None:
            self.image_name = image_name
        if domain_status is not None:
            self.domain_status = domain_status
        if rejoin_able is not None:
            self.rejoin_able = rejoin_able
        if product is not None:
            self.product = product
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this BatchCheckRejoinDomainResult.

        桌面ID。

        :return: The desktop_id of this BatchCheckRejoinDomainResult.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this BatchCheckRejoinDomainResult.

        桌面ID。

        :param desktop_id: The desktop_id of this BatchCheckRejoinDomainResult.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this BatchCheckRejoinDomainResult.

        桌面名称。

        :return: The desktop_name of this BatchCheckRejoinDomainResult.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this BatchCheckRejoinDomainResult.

        桌面名称。

        :param desktop_name: The desktop_name of this BatchCheckRejoinDomainResult.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def image_name(self):
        r"""Gets the image_name of this BatchCheckRejoinDomainResult.

        镜像名称。

        :return: The image_name of this BatchCheckRejoinDomainResult.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this BatchCheckRejoinDomainResult.

        镜像名称。

        :param image_name: The image_name of this BatchCheckRejoinDomainResult.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def domain_status(self):
        r"""Gets the domain_status of this BatchCheckRejoinDomainResult.

        加域状态。|- 1 正常。 2 脱域。 3 未上报。

        :return: The domain_status of this BatchCheckRejoinDomainResult.
        :rtype: int
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        r"""Sets the domain_status of this BatchCheckRejoinDomainResult.

        加域状态。|- 1 正常。 2 脱域。 3 未上报。

        :param domain_status: The domain_status of this BatchCheckRejoinDomainResult.
        :type domain_status: int
        """
        self._domain_status = domain_status

    @property
    def rejoin_able(self):
        r"""Gets the rejoin_able of this BatchCheckRejoinDomainResult.

        是否可以加域。

        :return: The rejoin_able of this BatchCheckRejoinDomainResult.
        :rtype: bool
        """
        return self._rejoin_able

    @rejoin_able.setter
    def rejoin_able(self, rejoin_able):
        r"""Sets the rejoin_able of this BatchCheckRejoinDomainResult.

        是否可以加域。

        :param rejoin_able: The rejoin_able of this BatchCheckRejoinDomainResult.
        :type rejoin_able: bool
        """
        self._rejoin_able = rejoin_able

    @property
    def product(self):
        r"""Gets the product of this BatchCheckRejoinDomainResult.

        :return: The product of this BatchCheckRejoinDomainResult.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        """
        return self._product

    @product.setter
    def product(self, product):
        r"""Sets the product of this BatchCheckRejoinDomainResult.

        :param product: The product of this BatchCheckRejoinDomainResult.
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        """
        self._product = product

    @property
    def error_code(self):
        r"""Gets the error_code of this BatchCheckRejoinDomainResult.

        错误码。

        :return: The error_code of this BatchCheckRejoinDomainResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this BatchCheckRejoinDomainResult.

        错误码。

        :param error_code: The error_code of this BatchCheckRejoinDomainResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BatchCheckRejoinDomainResult.

        错误信息。

        :return: The error_msg of this BatchCheckRejoinDomainResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BatchCheckRejoinDomainResult.

        错误信息。

        :param error_msg: The error_msg of this BatchCheckRejoinDomainResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, BatchCheckRejoinDomainResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

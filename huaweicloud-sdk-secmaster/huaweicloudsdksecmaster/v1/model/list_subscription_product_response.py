# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionProductResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic': 'ProductRspBasic',
        'standard': 'ProductRspStandard',
        'professional': 'ProductRspProfessional',
        'large_screen': 'ProductRspLargeScreen',
        'log_collection': 'ProductRspLogCollection',
        'log_retention': 'ProductRspLogRetention',
        'log_analysis': 'ProductRspLogAnalysis',
        'soar': 'ProductRspSoar'
    }

    attribute_map = {
        'basic': 'basic',
        'standard': 'standard',
        'professional': 'professional',
        'large_screen': 'large_screen',
        'log_collection': 'log_collection',
        'log_retention': 'log_retention',
        'log_analysis': 'log_analysis',
        'soar': 'soar'
    }

    def __init__(self, basic=None, standard=None, professional=None, large_screen=None, log_collection=None, log_retention=None, log_analysis=None, soar=None):
        r"""ListSubscriptionProductResponse

        The model defined in huaweicloud sdk

        :param basic: 
        :type basic: :class:`huaweicloudsdksecmaster.v1.ProductRspBasic`
        :param standard: 
        :type standard: :class:`huaweicloudsdksecmaster.v1.ProductRspStandard`
        :param professional: 
        :type professional: :class:`huaweicloudsdksecmaster.v1.ProductRspProfessional`
        :param large_screen: 
        :type large_screen: :class:`huaweicloudsdksecmaster.v1.ProductRspLargeScreen`
        :param log_collection: 
        :type log_collection: :class:`huaweicloudsdksecmaster.v1.ProductRspLogCollection`
        :param log_retention: 
        :type log_retention: :class:`huaweicloudsdksecmaster.v1.ProductRspLogRetention`
        :param log_analysis: 
        :type log_analysis: :class:`huaweicloudsdksecmaster.v1.ProductRspLogAnalysis`
        :param soar: 
        :type soar: :class:`huaweicloudsdksecmaster.v1.ProductRspSoar`
        """
        
        super().__init__()

        self._basic = None
        self._standard = None
        self._professional = None
        self._large_screen = None
        self._log_collection = None
        self._log_retention = None
        self._log_analysis = None
        self._soar = None
        self.discriminator = None

        if basic is not None:
            self.basic = basic
        if standard is not None:
            self.standard = standard
        if professional is not None:
            self.professional = professional
        if large_screen is not None:
            self.large_screen = large_screen
        if log_collection is not None:
            self.log_collection = log_collection
        if log_retention is not None:
            self.log_retention = log_retention
        if log_analysis is not None:
            self.log_analysis = log_analysis
        if soar is not None:
            self.soar = soar

    @property
    def basic(self):
        r"""Gets the basic of this ListSubscriptionProductResponse.

        :return: The basic of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspBasic`
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        r"""Sets the basic of this ListSubscriptionProductResponse.

        :param basic: The basic of this ListSubscriptionProductResponse.
        :type basic: :class:`huaweicloudsdksecmaster.v1.ProductRspBasic`
        """
        self._basic = basic

    @property
    def standard(self):
        r"""Gets the standard of this ListSubscriptionProductResponse.

        :return: The standard of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspStandard`
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListSubscriptionProductResponse.

        :param standard: The standard of this ListSubscriptionProductResponse.
        :type standard: :class:`huaweicloudsdksecmaster.v1.ProductRspStandard`
        """
        self._standard = standard

    @property
    def professional(self):
        r"""Gets the professional of this ListSubscriptionProductResponse.

        :return: The professional of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspProfessional`
        """
        return self._professional

    @professional.setter
    def professional(self, professional):
        r"""Sets the professional of this ListSubscriptionProductResponse.

        :param professional: The professional of this ListSubscriptionProductResponse.
        :type professional: :class:`huaweicloudsdksecmaster.v1.ProductRspProfessional`
        """
        self._professional = professional

    @property
    def large_screen(self):
        r"""Gets the large_screen of this ListSubscriptionProductResponse.

        :return: The large_screen of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspLargeScreen`
        """
        return self._large_screen

    @large_screen.setter
    def large_screen(self, large_screen):
        r"""Sets the large_screen of this ListSubscriptionProductResponse.

        :param large_screen: The large_screen of this ListSubscriptionProductResponse.
        :type large_screen: :class:`huaweicloudsdksecmaster.v1.ProductRspLargeScreen`
        """
        self._large_screen = large_screen

    @property
    def log_collection(self):
        r"""Gets the log_collection of this ListSubscriptionProductResponse.

        :return: The log_collection of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspLogCollection`
        """
        return self._log_collection

    @log_collection.setter
    def log_collection(self, log_collection):
        r"""Sets the log_collection of this ListSubscriptionProductResponse.

        :param log_collection: The log_collection of this ListSubscriptionProductResponse.
        :type log_collection: :class:`huaweicloudsdksecmaster.v1.ProductRspLogCollection`
        """
        self._log_collection = log_collection

    @property
    def log_retention(self):
        r"""Gets the log_retention of this ListSubscriptionProductResponse.

        :return: The log_retention of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspLogRetention`
        """
        return self._log_retention

    @log_retention.setter
    def log_retention(self, log_retention):
        r"""Sets the log_retention of this ListSubscriptionProductResponse.

        :param log_retention: The log_retention of this ListSubscriptionProductResponse.
        :type log_retention: :class:`huaweicloudsdksecmaster.v1.ProductRspLogRetention`
        """
        self._log_retention = log_retention

    @property
    def log_analysis(self):
        r"""Gets the log_analysis of this ListSubscriptionProductResponse.

        :return: The log_analysis of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspLogAnalysis`
        """
        return self._log_analysis

    @log_analysis.setter
    def log_analysis(self, log_analysis):
        r"""Sets the log_analysis of this ListSubscriptionProductResponse.

        :param log_analysis: The log_analysis of this ListSubscriptionProductResponse.
        :type log_analysis: :class:`huaweicloudsdksecmaster.v1.ProductRspLogAnalysis`
        """
        self._log_analysis = log_analysis

    @property
    def soar(self):
        r"""Gets the soar of this ListSubscriptionProductResponse.

        :return: The soar of this ListSubscriptionProductResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ProductRspSoar`
        """
        return self._soar

    @soar.setter
    def soar(self, soar):
        r"""Sets the soar of this ListSubscriptionProductResponse.

        :param soar: The soar of this ListSubscriptionProductResponse.
        :type soar: :class:`huaweicloudsdksecmaster.v1.ProductRspSoar`
        """
        self._soar = soar

    def to_dict(self):
        import warnings
        warnings.warn("ListSubscriptionProductResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListSubscriptionProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

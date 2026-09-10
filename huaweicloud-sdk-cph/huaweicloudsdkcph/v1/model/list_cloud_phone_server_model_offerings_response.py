# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneServerModelOfferingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'count': 'int',
        'models': 'list[ListCloudPhoneServersModelOfferingsResponseBodyModels]',
        'page_info': 'ListCloudPhoneServersModelOfferingsResponseBodyPageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'count': 'count',
        'models': 'models',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, count=None, models=None, page_info=None):
        r"""ListCloudPhoneServerModelOfferingsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param count: 规格总数。
        :type count: int
        :param models: 云手机服务器规格信息
        :type models: list[:class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyModels`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyPageInfo`
        """
        
        super().__init__()

        self._request_id = None
        self._count = None
        self._models = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if count is not None:
            self.count = count
        if models is not None:
            self.models = models
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListCloudPhoneServerModelOfferingsResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListCloudPhoneServerModelOfferingsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListCloudPhoneServerModelOfferingsResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListCloudPhoneServerModelOfferingsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def count(self):
        r"""Gets the count of this ListCloudPhoneServerModelOfferingsResponse.

        规格总数。

        :return: The count of this ListCloudPhoneServerModelOfferingsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListCloudPhoneServerModelOfferingsResponse.

        规格总数。

        :param count: The count of this ListCloudPhoneServerModelOfferingsResponse.
        :type count: int
        """
        self._count = count

    @property
    def models(self):
        r"""Gets the models of this ListCloudPhoneServerModelOfferingsResponse.

        云手机服务器规格信息

        :return: The models of this ListCloudPhoneServerModelOfferingsResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyModels`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ListCloudPhoneServerModelOfferingsResponse.

        云手机服务器规格信息

        :param models: The models of this ListCloudPhoneServerModelOfferingsResponse.
        :type models: list[:class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyModels`]
        """
        self._models = models

    @property
    def page_info(self):
        r"""Gets the page_info of this ListCloudPhoneServerModelOfferingsResponse.

        :return: The page_info of this ListCloudPhoneServerModelOfferingsResponse.
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListCloudPhoneServerModelOfferingsResponse.

        :param page_info: The page_info of this ListCloudPhoneServerModelOfferingsResponse.
        :type page_info: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyPageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListCloudPhoneServerModelOfferingsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCloudPhoneServerModelOfferingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

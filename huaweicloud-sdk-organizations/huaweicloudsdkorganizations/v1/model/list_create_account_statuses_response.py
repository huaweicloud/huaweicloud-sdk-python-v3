# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCreateAccountStatusesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_account_statuses': 'list[CreateAccountStatusDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'create_account_statuses': 'create_account_statuses',
        'page_info': 'page_info'
    }

    def __init__(self, create_account_statuses=None, page_info=None):
        """ListCreateAccountStatusesResponse

        The model defined in huaweicloud sdk

        :param create_account_statuses: 包含有关请求的详细信息的对象列表。
        :type create_account_statuses: list[:class:`huaweicloudsdkorganizations.v1.CreateAccountStatusDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListCreateAccountStatusesResponse, self).__init__()

        self._create_account_statuses = None
        self._page_info = None
        self.discriminator = None

        if create_account_statuses is not None:
            self.create_account_statuses = create_account_statuses
        if page_info is not None:
            self.page_info = page_info

    @property
    def create_account_statuses(self):
        """Gets the create_account_statuses of this ListCreateAccountStatusesResponse.

        包含有关请求的详细信息的对象列表。

        :return: The create_account_statuses of this ListCreateAccountStatusesResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.CreateAccountStatusDto`]
        """
        return self._create_account_statuses

    @create_account_statuses.setter
    def create_account_statuses(self, create_account_statuses):
        """Sets the create_account_statuses of this ListCreateAccountStatusesResponse.

        包含有关请求的详细信息的对象列表。

        :param create_account_statuses: The create_account_statuses of this ListCreateAccountStatusesResponse.
        :type create_account_statuses: list[:class:`huaweicloudsdkorganizations.v1.CreateAccountStatusDto`]
        """
        self._create_account_statuses = create_account_statuses

    @property
    def page_info(self):
        """Gets the page_info of this ListCreateAccountStatusesResponse.

        :return: The page_info of this ListCreateAccountStatusesResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCreateAccountStatusesResponse.

        :param page_info: The page_info of this ListCreateAccountStatusesResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListCreateAccountStatusesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

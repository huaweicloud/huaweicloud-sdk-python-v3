# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_instances': 'list[ApplicationInstanceDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'application_instances': 'application_instances',
        'page_info': 'page_info'
    }

    def __init__(self, application_instances=None, page_info=None):
        r"""ListApplicationInstancesResponse

        The model defined in huaweicloud sdk

        :param application_instances: 应用程序实例列表
        :type application_instances: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationInstanceDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListApplicationInstancesResponse, self).__init__()

        self._application_instances = None
        self._page_info = None
        self.discriminator = None

        if application_instances is not None:
            self.application_instances = application_instances
        if page_info is not None:
            self.page_info = page_info

    @property
    def application_instances(self):
        r"""Gets the application_instances of this ListApplicationInstancesResponse.

        应用程序实例列表

        :return: The application_instances of this ListApplicationInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationInstanceDto`]
        """
        return self._application_instances

    @application_instances.setter
    def application_instances(self, application_instances):
        r"""Sets the application_instances of this ListApplicationInstancesResponse.

        应用程序实例列表

        :param application_instances: The application_instances of this ListApplicationInstancesResponse.
        :type application_instances: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationInstanceDto`]
        """
        self._application_instances = application_instances

    @property
    def page_info(self):
        r"""Gets the page_info of this ListApplicationInstancesResponse.

        :return: The page_info of this ListApplicationInstancesResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListApplicationInstancesResponse.

        :param page_info: The page_info of this ListApplicationInstancesResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
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
        if not isinstance(other, ListApplicationInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

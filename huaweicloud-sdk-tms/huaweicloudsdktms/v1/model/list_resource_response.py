# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[Resources]',
        'errors': 'list[Errors]',
        'total_count': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'errors': 'errors',
        'total_count': 'total_count'
    }

    def __init__(self, resources=None, errors=None, total_count=None):
        """ListResourceResponse

        The model defined in huaweicloud sdk

        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdktms.v1.Resources`]
        :param errors: 查询标签下的资源
        :type errors: list[:class:`huaweicloudsdktms.v1.Errors`]
        :param total_count: 标签下的资源总数
        :type total_count: int
        """
        
        super(ListResourceResponse, self).__init__()

        self._resources = None
        self._errors = None
        self._total_count = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if errors is not None:
            self.errors = errors
        if total_count is not None:
            self.total_count = total_count

    @property
    def resources(self):
        """Gets the resources of this ListResourceResponse.

        资源列表

        :return: The resources of this ListResourceResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.Resources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListResourceResponse.

        资源列表

        :param resources: The resources of this ListResourceResponse.
        :type resources: list[:class:`huaweicloudsdktms.v1.Resources`]
        """
        self._resources = resources

    @property
    def errors(self):
        """Gets the errors of this ListResourceResponse.

        查询标签下的资源

        :return: The errors of this ListResourceResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.Errors`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ListResourceResponse.

        查询标签下的资源

        :param errors: The errors of this ListResourceResponse.
        :type errors: list[:class:`huaweicloudsdktms.v1.Errors`]
        """
        self._errors = errors

    @property
    def total_count(self):
        """Gets the total_count of this ListResourceResponse.

        标签下的资源总数

        :return: The total_count of this ListResourceResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListResourceResponse.

        标签下的资源总数

        :param total_count: The total_count of this ListResourceResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

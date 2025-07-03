# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLaunchTemplateVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'launch_template_versions': 'list[TemplateVersion]',
        'page_info': 'ResponsePageInfoV3',
        'x_request_id': 'str'
    }

    attribute_map = {
        'launch_template_versions': 'launch_template_versions',
        'page_info': 'page_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, launch_template_versions=None, page_info=None, x_request_id=None):
        r"""ListLaunchTemplateVersionsResponse

        The model defined in huaweicloud sdk

        :param launch_template_versions: 模板版本列表
        :type launch_template_versions: list[:class:`huaweicloudsdkecs.v2.TemplateVersion`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkecs.v2.ResponsePageInfoV3`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListLaunchTemplateVersionsResponse, self).__init__()

        self._launch_template_versions = None
        self._page_info = None
        self._x_request_id = None
        self.discriminator = None

        if launch_template_versions is not None:
            self.launch_template_versions = launch_template_versions
        if page_info is not None:
            self.page_info = page_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def launch_template_versions(self):
        r"""Gets the launch_template_versions of this ListLaunchTemplateVersionsResponse.

        模板版本列表

        :return: The launch_template_versions of this ListLaunchTemplateVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.TemplateVersion`]
        """
        return self._launch_template_versions

    @launch_template_versions.setter
    def launch_template_versions(self, launch_template_versions):
        r"""Sets the launch_template_versions of this ListLaunchTemplateVersionsResponse.

        模板版本列表

        :param launch_template_versions: The launch_template_versions of this ListLaunchTemplateVersionsResponse.
        :type launch_template_versions: list[:class:`huaweicloudsdkecs.v2.TemplateVersion`]
        """
        self._launch_template_versions = launch_template_versions

    @property
    def page_info(self):
        r"""Gets the page_info of this ListLaunchTemplateVersionsResponse.

        :return: The page_info of this ListLaunchTemplateVersionsResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.ResponsePageInfoV3`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListLaunchTemplateVersionsResponse.

        :param page_info: The page_info of this ListLaunchTemplateVersionsResponse.
        :type page_info: :class:`huaweicloudsdkecs.v2.ResponsePageInfoV3`
        """
        self._page_info = page_info

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListLaunchTemplateVersionsResponse.

        :return: The x_request_id of this ListLaunchTemplateVersionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListLaunchTemplateVersionsResponse.

        :param x_request_id: The x_request_id of this ListLaunchTemplateVersionsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListLaunchTemplateVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

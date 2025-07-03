# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'launch_templates': 'list[LaunchTemplate]',
        'page_info': 'ResponsePageInfoV3',
        'x_request_id': 'str'
    }

    attribute_map = {
        'launch_templates': 'launch_templates',
        'page_info': 'page_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, launch_templates=None, page_info=None, x_request_id=None):
        r"""ListTemplatesResponse

        The model defined in huaweicloud sdk

        :param launch_templates: 模板列表
        :type launch_templates: list[:class:`huaweicloudsdkecs.v2.LaunchTemplate`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkecs.v2.ResponsePageInfoV3`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListTemplatesResponse, self).__init__()

        self._launch_templates = None
        self._page_info = None
        self._x_request_id = None
        self.discriminator = None

        if launch_templates is not None:
            self.launch_templates = launch_templates
        if page_info is not None:
            self.page_info = page_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def launch_templates(self):
        r"""Gets the launch_templates of this ListTemplatesResponse.

        模板列表

        :return: The launch_templates of this ListTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.LaunchTemplate`]
        """
        return self._launch_templates

    @launch_templates.setter
    def launch_templates(self, launch_templates):
        r"""Sets the launch_templates of this ListTemplatesResponse.

        模板列表

        :param launch_templates: The launch_templates of this ListTemplatesResponse.
        :type launch_templates: list[:class:`huaweicloudsdkecs.v2.LaunchTemplate`]
        """
        self._launch_templates = launch_templates

    @property
    def page_info(self):
        r"""Gets the page_info of this ListTemplatesResponse.

        :return: The page_info of this ListTemplatesResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.ResponsePageInfoV3`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListTemplatesResponse.

        :param page_info: The page_info of this ListTemplatesResponse.
        :type page_info: :class:`huaweicloudsdkecs.v2.ResponsePageInfoV3`
        """
        self._page_info = page_info

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListTemplatesResponse.

        :return: The x_request_id of this ListTemplatesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListTemplatesResponse.

        :param x_request_id: The x_request_id of this ListTemplatesResponse.
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
        if not isinstance(other, ListTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLaunchTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'launch_template_id': 'str'
    }

    attribute_map = {
        'launch_template_id': 'launch_template_id'
    }

    def __init__(self, launch_template_id=None):
        r"""DeleteLaunchTemplatesRequest

        The model defined in huaweicloud sdk

        :param launch_template_id: 模板ID。
        :type launch_template_id: str
        """
        
        

        self._launch_template_id = None
        self.discriminator = None

        self.launch_template_id = launch_template_id

    @property
    def launch_template_id(self):
        r"""Gets the launch_template_id of this DeleteLaunchTemplatesRequest.

        模板ID。

        :return: The launch_template_id of this DeleteLaunchTemplatesRequest.
        :rtype: str
        """
        return self._launch_template_id

    @launch_template_id.setter
    def launch_template_id(self, launch_template_id):
        r"""Sets the launch_template_id of this DeleteLaunchTemplatesRequest.

        模板ID。

        :param launch_template_id: The launch_template_id of this DeleteLaunchTemplatesRequest.
        :type launch_template_id: str
        """
        self._launch_template_id = launch_template_id

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
        if not isinstance(other, DeleteLaunchTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLaunchTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'launch_template': 'LaunchTemplateOption',
        'dry_run': 'bool'
    }

    attribute_map = {
        'launch_template': 'launch_template',
        'dry_run': 'dry_run'
    }

    def __init__(self, launch_template=None, dry_run=None):
        r"""CreateLaunchTemplateRequestBody

        The model defined in huaweicloud sdk

        :param launch_template: 
        :type launch_template: :class:`huaweicloudsdkecs.v2.LaunchTemplateOption`
        :param dry_run: 预检，只校验权限等初级信息。
        :type dry_run: bool
        """
        
        

        self._launch_template = None
        self._dry_run = None
        self.discriminator = None

        self.launch_template = launch_template
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def launch_template(self):
        r"""Gets the launch_template of this CreateLaunchTemplateRequestBody.

        :return: The launch_template of this CreateLaunchTemplateRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.LaunchTemplateOption`
        """
        return self._launch_template

    @launch_template.setter
    def launch_template(self, launch_template):
        r"""Sets the launch_template of this CreateLaunchTemplateRequestBody.

        :param launch_template: The launch_template of this CreateLaunchTemplateRequestBody.
        :type launch_template: :class:`huaweicloudsdkecs.v2.LaunchTemplateOption`
        """
        self._launch_template = launch_template

    @property
    def dry_run(self):
        r"""Gets the dry_run of this CreateLaunchTemplateRequestBody.

        预检，只校验权限等初级信息。

        :return: The dry_run of this CreateLaunchTemplateRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this CreateLaunchTemplateRequestBody.

        预检，只校验权限等初级信息。

        :param dry_run: The dry_run of this CreateLaunchTemplateRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, CreateLaunchTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

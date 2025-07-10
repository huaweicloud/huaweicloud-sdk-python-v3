# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildUpdateSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'run_workspace': 'str',
        'run_image_status': 'RunImageStatusEnum'
    }

    attribute_map = {
        'run_workspace': 'run_workspace',
        'run_image_status': 'run_image_status'
    }

    def __init__(self, run_workspace=None, run_image_status=None):
        r"""BuildUpdateSrlz

        The model defined in huaweicloud sdk

        :param run_workspace: 运行目录
        :type run_workspace: str
        :param run_image_status: 运行镜像状态  * &#x60;0&#x60; - Success * &#x60;100&#x60; - Init * &#x60;101&#x60; - Init Failed * &#x60;200&#x60; - To Push * &#x60;201&#x60; - Uploading
        :type run_image_status: :class:`huaweicloudsdkoctopus.v2.RunImageStatusEnum`
        """
        
        

        self._run_workspace = None
        self._run_image_status = None
        self.discriminator = None

        if run_workspace is not None:
            self.run_workspace = run_workspace
        self.run_image_status = run_image_status

    @property
    def run_workspace(self):
        r"""Gets the run_workspace of this BuildUpdateSrlz.

        运行目录

        :return: The run_workspace of this BuildUpdateSrlz.
        :rtype: str
        """
        return self._run_workspace

    @run_workspace.setter
    def run_workspace(self, run_workspace):
        r"""Sets the run_workspace of this BuildUpdateSrlz.

        运行目录

        :param run_workspace: The run_workspace of this BuildUpdateSrlz.
        :type run_workspace: str
        """
        self._run_workspace = run_workspace

    @property
    def run_image_status(self):
        r"""Gets the run_image_status of this BuildUpdateSrlz.

        运行镜像状态  * `0` - Success * `100` - Init * `101` - Init Failed * `200` - To Push * `201` - Uploading

        :return: The run_image_status of this BuildUpdateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.RunImageStatusEnum`
        """
        return self._run_image_status

    @run_image_status.setter
    def run_image_status(self, run_image_status):
        r"""Sets the run_image_status of this BuildUpdateSrlz.

        运行镜像状态  * `0` - Success * `100` - Init * `101` - Init Failed * `200` - To Push * `201` - Uploading

        :param run_image_status: The run_image_status of this BuildUpdateSrlz.
        :type run_image_status: :class:`huaweicloudsdkoctopus.v2.RunImageStatusEnum`
        """
        self._run_image_status = run_image_status

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
        if not isinstance(other, BuildUpdateSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachInstancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktops': 'list[AttachInstancesDesktopInfo]',
        'image_type': 'str',
        'image_id': 'str',
        'os_type': 'str',
        'enterprise_project_id': 'str',
        'desktop_name_policy_id': 'str'
    }

    attribute_map = {
        'desktops': 'desktops',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'os_type': 'os_type',
        'enterprise_project_id': 'enterprise_project_id',
        'desktop_name_policy_id': 'desktop_name_policy_id'
    }

    def __init__(self, desktops=None, image_type=None, image_id=None, os_type=None, enterprise_project_id=None, desktop_name_policy_id=None):
        """AttachInstancesReq

        The model defined in huaweicloud sdk

        :param desktops: 桌面信息列表。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        :param image_type: 镜像类型，涉及变更镜像时需传（可选）
        :type image_type: str
        :param image_id: 模板ID，涉及变更镜像时需传（可选）
        :type image_id: str
        :param os_type: os类型，涉及变更镜像时需传（可选）
        :type os_type: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0\&quot;
        :type enterprise_project_id: str
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。
        :type desktop_name_policy_id: str
        """
        
        

        self._desktops = None
        self._image_type = None
        self._image_id = None
        self._os_type = None
        self._enterprise_project_id = None
        self._desktop_name_policy_id = None
        self.discriminator = None

        self.desktops = desktops
        if image_type is not None:
            self.image_type = image_type
        if image_id is not None:
            self.image_id = image_id
        if os_type is not None:
            self.os_type = os_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id

    @property
    def desktops(self):
        """Gets the desktops of this AttachInstancesReq.

        桌面信息列表。

        :return: The desktops of this AttachInstancesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this AttachInstancesReq.

        桌面信息列表。

        :param desktops: The desktops of this AttachInstancesReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        self._desktops = desktops

    @property
    def image_type(self):
        """Gets the image_type of this AttachInstancesReq.

        镜像类型，涉及变更镜像时需传（可选）

        :return: The image_type of this AttachInstancesReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this AttachInstancesReq.

        镜像类型，涉及变更镜像时需传（可选）

        :param image_type: The image_type of this AttachInstancesReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        """Gets the image_id of this AttachInstancesReq.

        模板ID，涉及变更镜像时需传（可选）

        :return: The image_id of this AttachInstancesReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this AttachInstancesReq.

        模板ID，涉及变更镜像时需传（可选）

        :param image_id: The image_id of this AttachInstancesReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def os_type(self):
        """Gets the os_type of this AttachInstancesReq.

        os类型，涉及变更镜像时需传（可选）

        :return: The os_type of this AttachInstancesReq.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this AttachInstancesReq.

        os类型，涉及变更镜像时需传（可选）

        :param os_type: The os_type of this AttachInstancesReq.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AttachInstancesReq.

        企业项目ID，默认\"0\"

        :return: The enterprise_project_id of this AttachInstancesReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AttachInstancesReq.

        企业项目ID，默认\"0\"

        :param enterprise_project_id: The enterprise_project_id of this AttachInstancesReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def desktop_name_policy_id(self):
        """Gets the desktop_name_policy_id of this AttachInstancesReq.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :return: The desktop_name_policy_id of this AttachInstancesReq.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        """Sets the desktop_name_policy_id of this AttachInstancesReq.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :param desktop_name_policy_id: The desktop_name_policy_id of this AttachInstancesReq.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

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
        if not isinstance(other, AttachInstancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

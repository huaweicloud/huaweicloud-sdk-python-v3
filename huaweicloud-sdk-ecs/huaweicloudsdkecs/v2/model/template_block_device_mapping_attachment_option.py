# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateBlockDeviceMappingAttachmentOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'boot_index': 'int',
        'delete_on_termination': 'bool'
    }

    attribute_map = {
        'boot_index': 'boot_index',
        'delete_on_termination': 'delete_on_termination'
    }

    def __init__(self, boot_index=None, delete_on_termination=None):
        r"""TemplateBlockDeviceMappingAttachmentOption

        The model defined in huaweicloud sdk

        :param boot_index: 盘在虚拟机上的挂载顺序，0表示启动盘
        :type boot_index: int
        :param delete_on_termination: 卷是否随实例一同释放 默认系统盘设置为true随实例释放，数据盘设置为false不随实例释放
        :type delete_on_termination: bool
        """
        
        

        self._boot_index = None
        self._delete_on_termination = None
        self.discriminator = None

        if boot_index is not None:
            self.boot_index = boot_index
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination

    @property
    def boot_index(self):
        r"""Gets the boot_index of this TemplateBlockDeviceMappingAttachmentOption.

        盘在虚拟机上的挂载顺序，0表示启动盘

        :return: The boot_index of this TemplateBlockDeviceMappingAttachmentOption.
        :rtype: int
        """
        return self._boot_index

    @boot_index.setter
    def boot_index(self, boot_index):
        r"""Sets the boot_index of this TemplateBlockDeviceMappingAttachmentOption.

        盘在虚拟机上的挂载顺序，0表示启动盘

        :param boot_index: The boot_index of this TemplateBlockDeviceMappingAttachmentOption.
        :type boot_index: int
        """
        self._boot_index = boot_index

    @property
    def delete_on_termination(self):
        r"""Gets the delete_on_termination of this TemplateBlockDeviceMappingAttachmentOption.

        卷是否随实例一同释放 默认系统盘设置为true随实例释放，数据盘设置为false不随实例释放

        :return: The delete_on_termination of this TemplateBlockDeviceMappingAttachmentOption.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        r"""Sets the delete_on_termination of this TemplateBlockDeviceMappingAttachmentOption.

        卷是否随实例一同释放 默认系统盘设置为true随实例释放，数据盘设置为false不随实例释放

        :param delete_on_termination: The delete_on_termination of this TemplateBlockDeviceMappingAttachmentOption.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

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
        if not isinstance(other, TemplateBlockDeviceMappingAttachmentOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

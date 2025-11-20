# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceSharedConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'optional_project_ids': 'list[str]',
        'no_need_review': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'optional_project_ids': 'optional_project_ids',
        'no_need_review': 'no_need_review'
    }

    def __init__(self, enable=None, optional_project_ids=None, no_need_review=None):
        r"""ServiceSharedConfig

        The model defined in huaweicloud sdk

        :param enable: 开启共享配置
        :type enable: bool
        :param optional_project_ids: 可选的共享租户列表
        :type optional_project_ids: list[str]
        :param no_need_review: 共享免审核
        :type no_need_review: bool
        """
        
        

        self._enable = None
        self._optional_project_ids = None
        self._no_need_review = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if optional_project_ids is not None:
            self.optional_project_ids = optional_project_ids
        if no_need_review is not None:
            self.no_need_review = no_need_review

    @property
    def enable(self):
        r"""Gets the enable of this ServiceSharedConfig.

        开启共享配置

        :return: The enable of this ServiceSharedConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ServiceSharedConfig.

        开启共享配置

        :param enable: The enable of this ServiceSharedConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def optional_project_ids(self):
        r"""Gets the optional_project_ids of this ServiceSharedConfig.

        可选的共享租户列表

        :return: The optional_project_ids of this ServiceSharedConfig.
        :rtype: list[str]
        """
        return self._optional_project_ids

    @optional_project_ids.setter
    def optional_project_ids(self, optional_project_ids):
        r"""Sets the optional_project_ids of this ServiceSharedConfig.

        可选的共享租户列表

        :param optional_project_ids: The optional_project_ids of this ServiceSharedConfig.
        :type optional_project_ids: list[str]
        """
        self._optional_project_ids = optional_project_ids

    @property
    def no_need_review(self):
        r"""Gets the no_need_review of this ServiceSharedConfig.

        共享免审核

        :return: The no_need_review of this ServiceSharedConfig.
        :rtype: bool
        """
        return self._no_need_review

    @no_need_review.setter
    def no_need_review(self, no_need_review):
        r"""Sets the no_need_review of this ServiceSharedConfig.

        共享免审核

        :param no_need_review: The no_need_review of this ServiceSharedConfig.
        :type no_need_review: bool
        """
        self._no_need_review = no_need_review

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceSharedConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareComponentConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_envs': 'list[ComponentConfigEnvs]',
        'remove_envs': 'list[ComponentConfigEnvs]',
        'modify_envs': 'list[ComponentConfigCompareResultModifyEnvs]'
    }

    attribute_map = {
        'add_envs': 'add_envs',
        'remove_envs': 'remove_envs',
        'modify_envs': 'modify_envs'
    }

    def __init__(self, add_envs=None, remove_envs=None, modify_envs=None):
        """CompareComponentConfigurationResponse

        The model defined in huaweicloud sdk

        :param add_envs: 
        :type add_envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        :param remove_envs: 
        :type remove_envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        :param modify_envs: 
        :type modify_envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigCompareResultModifyEnvs`]
        """
        
        super(CompareComponentConfigurationResponse, self).__init__()

        self._add_envs = None
        self._remove_envs = None
        self._modify_envs = None
        self.discriminator = None

        if add_envs is not None:
            self.add_envs = add_envs
        if remove_envs is not None:
            self.remove_envs = remove_envs
        if modify_envs is not None:
            self.modify_envs = modify_envs

    @property
    def add_envs(self):
        """Gets the add_envs of this CompareComponentConfigurationResponse.

        :return: The add_envs of this CompareComponentConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        return self._add_envs

    @add_envs.setter
    def add_envs(self, add_envs):
        """Sets the add_envs of this CompareComponentConfigurationResponse.

        :param add_envs: The add_envs of this CompareComponentConfigurationResponse.
        :type add_envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        self._add_envs = add_envs

    @property
    def remove_envs(self):
        """Gets the remove_envs of this CompareComponentConfigurationResponse.

        :return: The remove_envs of this CompareComponentConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        return self._remove_envs

    @remove_envs.setter
    def remove_envs(self, remove_envs):
        """Sets the remove_envs of this CompareComponentConfigurationResponse.

        :param remove_envs: The remove_envs of this CompareComponentConfigurationResponse.
        :type remove_envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        self._remove_envs = remove_envs

    @property
    def modify_envs(self):
        """Gets the modify_envs of this CompareComponentConfigurationResponse.

        :return: The modify_envs of this CompareComponentConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigCompareResultModifyEnvs`]
        """
        return self._modify_envs

    @modify_envs.setter
    def modify_envs(self, modify_envs):
        """Sets the modify_envs of this CompareComponentConfigurationResponse.

        :param modify_envs: The modify_envs of this CompareComponentConfigurationResponse.
        :type modify_envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigCompareResultModifyEnvs`]
        """
        self._modify_envs = modify_envs

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
        if not isinstance(other, CompareComponentConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

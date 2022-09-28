# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_delete': 'bool',
        'data_download': 'bool',
        'data_encrypted': 'bool',
        'data_share': 'bool'
    }

    attribute_map = {
        'data_delete': 'data_delete',
        'data_download': 'data_download',
        'data_encrypted': 'data_encrypted',
        'data_share': 'data_share'
    }

    def __init__(self, data_delete=None, data_download=None, data_encrypted=None, data_share=None):
        """ShowDataPolicyResponse

        The model defined in huaweicloud sdk

        :param data_delete: 项目级删除策略（true：允许项目数据删除操作，false：不允许删除操作，默认为true）
        :type data_delete: bool
        :param data_download: 项目级下载策略（true：允许项目数据下载操作，false：不允许下载操作，默认为true）
        :type data_download: bool
        :param data_encrypted: 项目级加密策略（true：允许项目数据加密操作，false：不允许加密操作，默认为false）
        :type data_encrypted: bool
        :param data_share: 项目级分享策略（true：允许项目数据拷贝/引用操作，false：不允许拷贝/引用操作，默认为true）
        :type data_share: bool
        """
        
        super(ShowDataPolicyResponse, self).__init__()

        self._data_delete = None
        self._data_download = None
        self._data_encrypted = None
        self._data_share = None
        self.discriminator = None

        if data_delete is not None:
            self.data_delete = data_delete
        if data_download is not None:
            self.data_download = data_download
        if data_encrypted is not None:
            self.data_encrypted = data_encrypted
        if data_share is not None:
            self.data_share = data_share

    @property
    def data_delete(self):
        """Gets the data_delete of this ShowDataPolicyResponse.

        项目级删除策略（true：允许项目数据删除操作，false：不允许删除操作，默认为true）

        :return: The data_delete of this ShowDataPolicyResponse.
        :rtype: bool
        """
        return self._data_delete

    @data_delete.setter
    def data_delete(self, data_delete):
        """Sets the data_delete of this ShowDataPolicyResponse.

        项目级删除策略（true：允许项目数据删除操作，false：不允许删除操作，默认为true）

        :param data_delete: The data_delete of this ShowDataPolicyResponse.
        :type data_delete: bool
        """
        self._data_delete = data_delete

    @property
    def data_download(self):
        """Gets the data_download of this ShowDataPolicyResponse.

        项目级下载策略（true：允许项目数据下载操作，false：不允许下载操作，默认为true）

        :return: The data_download of this ShowDataPolicyResponse.
        :rtype: bool
        """
        return self._data_download

    @data_download.setter
    def data_download(self, data_download):
        """Sets the data_download of this ShowDataPolicyResponse.

        项目级下载策略（true：允许项目数据下载操作，false：不允许下载操作，默认为true）

        :param data_download: The data_download of this ShowDataPolicyResponse.
        :type data_download: bool
        """
        self._data_download = data_download

    @property
    def data_encrypted(self):
        """Gets the data_encrypted of this ShowDataPolicyResponse.

        项目级加密策略（true：允许项目数据加密操作，false：不允许加密操作，默认为false）

        :return: The data_encrypted of this ShowDataPolicyResponse.
        :rtype: bool
        """
        return self._data_encrypted

    @data_encrypted.setter
    def data_encrypted(self, data_encrypted):
        """Sets the data_encrypted of this ShowDataPolicyResponse.

        项目级加密策略（true：允许项目数据加密操作，false：不允许加密操作，默认为false）

        :param data_encrypted: The data_encrypted of this ShowDataPolicyResponse.
        :type data_encrypted: bool
        """
        self._data_encrypted = data_encrypted

    @property
    def data_share(self):
        """Gets the data_share of this ShowDataPolicyResponse.

        项目级分享策略（true：允许项目数据拷贝/引用操作，false：不允许拷贝/引用操作，默认为true）

        :return: The data_share of this ShowDataPolicyResponse.
        :rtype: bool
        """
        return self._data_share

    @data_share.setter
    def data_share(self, data_share):
        """Sets the data_share of this ShowDataPolicyResponse.

        项目级分享策略（true：允许项目数据拷贝/引用操作，false：不允许拷贝/引用操作，默认为true）

        :param data_share: The data_share of this ShowDataPolicyResponse.
        :type data_share: bool
        """
        self._data_share = data_share

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
        if not isinstance(other, ShowDataPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

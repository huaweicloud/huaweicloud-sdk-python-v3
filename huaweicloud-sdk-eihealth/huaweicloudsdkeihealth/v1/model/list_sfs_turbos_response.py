# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSfsTurbosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sfs_turbos': 'list[SfsTurboRsp]',
        'count': 'int'
    }

    attribute_map = {
        'sfs_turbos': 'sfs_turbos',
        'count': 'count'
    }

    def __init__(self, sfs_turbos=None, count=None):
        r"""ListSfsTurbosResponse

        The model defined in huaweicloud sdk

        :param sfs_turbos: sfs-turbo资源列表。
        :type sfs_turbos: list[:class:`huaweicloudsdkeihealth.v1.SfsTurboRsp`]
        :param count: sfs-turbo资源总数。
        :type count: int
        """
        
        super(ListSfsTurbosResponse, self).__init__()

        self._sfs_turbos = None
        self._count = None
        self.discriminator = None

        if sfs_turbos is not None:
            self.sfs_turbos = sfs_turbos
        if count is not None:
            self.count = count

    @property
    def sfs_turbos(self):
        r"""Gets the sfs_turbos of this ListSfsTurbosResponse.

        sfs-turbo资源列表。

        :return: The sfs_turbos of this ListSfsTurbosResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SfsTurboRsp`]
        """
        return self._sfs_turbos

    @sfs_turbos.setter
    def sfs_turbos(self, sfs_turbos):
        r"""Sets the sfs_turbos of this ListSfsTurbosResponse.

        sfs-turbo资源列表。

        :param sfs_turbos: The sfs_turbos of this ListSfsTurbosResponse.
        :type sfs_turbos: list[:class:`huaweicloudsdkeihealth.v1.SfsTurboRsp`]
        """
        self._sfs_turbos = sfs_turbos

    @property
    def count(self):
        r"""Gets the count of this ListSfsTurbosResponse.

        sfs-turbo资源总数。

        :return: The count of this ListSfsTurbosResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSfsTurbosResponse.

        sfs-turbo资源总数。

        :param count: The count of this ListSfsTurbosResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListSfsTurbosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

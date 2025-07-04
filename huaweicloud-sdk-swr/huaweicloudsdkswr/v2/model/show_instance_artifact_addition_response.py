# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceArtifactAdditionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_histories': 'list[BuildHistory]',
        'total': 'int'
    }

    attribute_map = {
        'build_histories': 'build_histories',
        'total': 'total'
    }

    def __init__(self, build_histories=None, total=None):
        r"""ShowInstanceArtifactAdditionResponse

        The model defined in huaweicloud sdk

        :param build_histories: 构建历史列表
        :type build_histories: list[:class:`huaweicloudsdkswr.v2.BuildHistory`]
        :param total: 构建历史条数
        :type total: int
        """
        
        super(ShowInstanceArtifactAdditionResponse, self).__init__()

        self._build_histories = None
        self._total = None
        self.discriminator = None

        if build_histories is not None:
            self.build_histories = build_histories
        if total is not None:
            self.total = total

    @property
    def build_histories(self):
        r"""Gets the build_histories of this ShowInstanceArtifactAdditionResponse.

        构建历史列表

        :return: The build_histories of this ShowInstanceArtifactAdditionResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.BuildHistory`]
        """
        return self._build_histories

    @build_histories.setter
    def build_histories(self, build_histories):
        r"""Sets the build_histories of this ShowInstanceArtifactAdditionResponse.

        构建历史列表

        :param build_histories: The build_histories of this ShowInstanceArtifactAdditionResponse.
        :type build_histories: list[:class:`huaweicloudsdkswr.v2.BuildHistory`]
        """
        self._build_histories = build_histories

    @property
    def total(self):
        r"""Gets the total of this ShowInstanceArtifactAdditionResponse.

        构建历史条数

        :return: The total of this ShowInstanceArtifactAdditionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowInstanceArtifactAdditionResponse.

        构建历史条数

        :param total: The total of this ShowInstanceArtifactAdditionResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowInstanceArtifactAdditionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

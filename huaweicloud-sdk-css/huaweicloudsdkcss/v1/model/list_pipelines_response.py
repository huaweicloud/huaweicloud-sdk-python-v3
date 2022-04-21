# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pipelines': 'list[Pipelines]'
    }

    attribute_map = {
        'pipelines': 'pipelines'
    }

    def __init__(self, pipelines=None):
        """ListPipelinesResponse

        The model defined in huaweicloud sdk

        :param pipelines: pipeline列表。
        :type pipelines: list[:class:`huaweicloudsdkcss.v1.Pipelines`]
        """
        
        super(ListPipelinesResponse, self).__init__()

        self._pipelines = None
        self.discriminator = None

        if pipelines is not None:
            self.pipelines = pipelines

    @property
    def pipelines(self):
        """Gets the pipelines of this ListPipelinesResponse.

        pipeline列表。

        :return: The pipelines of this ListPipelinesResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.Pipelines`]
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        """Sets the pipelines of this ListPipelinesResponse.

        pipeline列表。

        :param pipelines: The pipelines of this ListPipelinesResponse.
        :type pipelines: list[:class:`huaweicloudsdkcss.v1.Pipelines`]
        """
        self._pipelines = pipelines

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
        if not isinstance(other, ListPipelinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

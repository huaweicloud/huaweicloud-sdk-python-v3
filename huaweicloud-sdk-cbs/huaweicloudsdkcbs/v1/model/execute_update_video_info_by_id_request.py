# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteUpdateVideoInfoByIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_id': 'str',
        'body': 'PutVideoInfo'
    }

    attribute_map = {
        'video_id': 'video_id',
        'body': 'body'
    }

    def __init__(self, video_id=None, body=None):
        """ExecuteUpdateVideoInfoByIdRequest

        The model defined in huaweicloud sdk

        :param video_id: 视频id
        :type video_id: str
        :param body: Body of the ExecuteUpdateVideoInfoByIdRequest
        :type body: :class:`huaweicloudsdkcbs.v1.PutVideoInfo`
        """
        
        

        self._video_id = None
        self._body = None
        self.discriminator = None

        self.video_id = video_id
        if body is not None:
            self.body = body

    @property
    def video_id(self):
        """Gets the video_id of this ExecuteUpdateVideoInfoByIdRequest.

        视频id

        :return: The video_id of this ExecuteUpdateVideoInfoByIdRequest.
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this ExecuteUpdateVideoInfoByIdRequest.

        视频id

        :param video_id: The video_id of this ExecuteUpdateVideoInfoByIdRequest.
        :type video_id: str
        """
        self._video_id = video_id

    @property
    def body(self):
        """Gets the body of this ExecuteUpdateVideoInfoByIdRequest.

        :return: The body of this ExecuteUpdateVideoInfoByIdRequest.
        :rtype: :class:`huaweicloudsdkcbs.v1.PutVideoInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExecuteUpdateVideoInfoByIdRequest.

        :param body: The body of this ExecuteUpdateVideoInfoByIdRequest.
        :type body: :class:`huaweicloudsdkcbs.v1.PutVideoInfo`
        """
        self._body = body

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
        if not isinstance(other, ExecuteUpdateVideoInfoByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

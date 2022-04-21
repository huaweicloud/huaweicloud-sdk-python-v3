# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteStreamForbiddenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'specify_project': 'str',
        'domain': 'str',
        'app_name': 'str',
        'stream_name': 'str'
    }

    attribute_map = {
        'specify_project': 'specify_project',
        'domain': 'domain',
        'app_name': 'app_name',
        'stream_name': 'stream_name'
    }

    def __init__(self, specify_project=None, domain=None, app_name=None, stream_name=None):
        """DeleteStreamForbiddenRequest

        The model defined in huaweicloud sdk

        :param specify_project: op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id
        :type specify_project: str
        :param domain: 推流域名
        :type domain: str
        :param app_name: RTMP应用名称
        :type app_name: str
        :param stream_name: 流名称
        :type stream_name: str
        """
        
        

        self._specify_project = None
        self._domain = None
        self._app_name = None
        self._stream_name = None
        self.discriminator = None

        if specify_project is not None:
            self.specify_project = specify_project
        self.domain = domain
        self.app_name = app_name
        self.stream_name = stream_name

    @property
    def specify_project(self):
        """Gets the specify_project of this DeleteStreamForbiddenRequest.

        op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id

        :return: The specify_project of this DeleteStreamForbiddenRequest.
        :rtype: str
        """
        return self._specify_project

    @specify_project.setter
    def specify_project(self, specify_project):
        """Sets the specify_project of this DeleteStreamForbiddenRequest.

        op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id

        :param specify_project: The specify_project of this DeleteStreamForbiddenRequest.
        :type specify_project: str
        """
        self._specify_project = specify_project

    @property
    def domain(self):
        """Gets the domain of this DeleteStreamForbiddenRequest.

        推流域名

        :return: The domain of this DeleteStreamForbiddenRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DeleteStreamForbiddenRequest.

        推流域名

        :param domain: The domain of this DeleteStreamForbiddenRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this DeleteStreamForbiddenRequest.

        RTMP应用名称

        :return: The app_name of this DeleteStreamForbiddenRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this DeleteStreamForbiddenRequest.

        RTMP应用名称

        :param app_name: The app_name of this DeleteStreamForbiddenRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this DeleteStreamForbiddenRequest.

        流名称

        :return: The stream_name of this DeleteStreamForbiddenRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this DeleteStreamForbiddenRequest.

        流名称

        :param stream_name: The stream_name of this DeleteStreamForbiddenRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

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
        if not isinstance(other, DeleteStreamForbiddenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

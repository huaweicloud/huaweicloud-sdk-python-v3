# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineBasicDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'web_url': 'str',
        'sha': 'str',
        'ref': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'web_url': 'web_url',
        'sha': 'sha',
        'ref': 'ref',
        'status': 'status'
    }

    def __init__(self, id=None, web_url=None, sha=None, ref=None, status=None):
        r"""PipelineBasicDto

        The model defined in huaweicloud sdk

        :param id: 流水线id
        :type id: int
        :param web_url: 流水线url
        :type web_url: str
        :param sha: 流水线关联sha值
        :type sha: str
        :param ref: 流水线ref
        :type ref: str
        :param status: 流水线状态
        :type status: str
        """
        
        

        self._id = None
        self._web_url = None
        self._sha = None
        self._ref = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if web_url is not None:
            self.web_url = web_url
        if sha is not None:
            self.sha = sha
        if ref is not None:
            self.ref = ref
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this PipelineBasicDto.

        流水线id

        :return: The id of this PipelineBasicDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PipelineBasicDto.

        流水线id

        :param id: The id of this PipelineBasicDto.
        :type id: int
        """
        self._id = id

    @property
    def web_url(self):
        r"""Gets the web_url of this PipelineBasicDto.

        流水线url

        :return: The web_url of this PipelineBasicDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this PipelineBasicDto.

        流水线url

        :param web_url: The web_url of this PipelineBasicDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def sha(self):
        r"""Gets the sha of this PipelineBasicDto.

        流水线关联sha值

        :return: The sha of this PipelineBasicDto.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this PipelineBasicDto.

        流水线关联sha值

        :param sha: The sha of this PipelineBasicDto.
        :type sha: str
        """
        self._sha = sha

    @property
    def ref(self):
        r"""Gets the ref of this PipelineBasicDto.

        流水线ref

        :return: The ref of this PipelineBasicDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this PipelineBasicDto.

        流水线ref

        :param ref: The ref of this PipelineBasicDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def status(self):
        r"""Gets the status of this PipelineBasicDto.

        流水线状态

        :return: The status of this PipelineBasicDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PipelineBasicDto.

        流水线状态

        :param status: The status of this PipelineBasicDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PipelineBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

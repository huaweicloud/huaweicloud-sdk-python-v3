# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecificCommitInfoLastPipeline:

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
        'sha': 'str',
        'ref': 'str',
        'status': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sha': 'sha',
        'ref': 'ref',
        'status': 'status',
        'web_url': 'web_url'
    }

    def __init__(self, id=None, sha=None, ref=None, status=None, web_url=None):
        """SpecificCommitInfoLastPipeline

        The model defined in huaweicloud sdk

        :param id: 流水线id
        :type id: int
        :param sha: 提交对应的SHA id
        :type sha: str
        :param ref: 分支名
        :type ref: str
        :param status: 流水线状态
        :type status: str
        :param web_url: 流水线url
        :type web_url: str
        """
        
        

        self._id = None
        self._sha = None
        self._ref = None
        self._status = None
        self._web_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sha is not None:
            self.sha = sha
        if ref is not None:
            self.ref = ref
        if status is not None:
            self.status = status
        if web_url is not None:
            self.web_url = web_url

    @property
    def id(self):
        """Gets the id of this SpecificCommitInfoLastPipeline.

        流水线id

        :return: The id of this SpecificCommitInfoLastPipeline.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpecificCommitInfoLastPipeline.

        流水线id

        :param id: The id of this SpecificCommitInfoLastPipeline.
        :type id: int
        """
        self._id = id

    @property
    def sha(self):
        """Gets the sha of this SpecificCommitInfoLastPipeline.

        提交对应的SHA id

        :return: The sha of this SpecificCommitInfoLastPipeline.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this SpecificCommitInfoLastPipeline.

        提交对应的SHA id

        :param sha: The sha of this SpecificCommitInfoLastPipeline.
        :type sha: str
        """
        self._sha = sha

    @property
    def ref(self):
        """Gets the ref of this SpecificCommitInfoLastPipeline.

        分支名

        :return: The ref of this SpecificCommitInfoLastPipeline.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this SpecificCommitInfoLastPipeline.

        分支名

        :param ref: The ref of this SpecificCommitInfoLastPipeline.
        :type ref: str
        """
        self._ref = ref

    @property
    def status(self):
        """Gets the status of this SpecificCommitInfoLastPipeline.

        流水线状态

        :return: The status of this SpecificCommitInfoLastPipeline.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SpecificCommitInfoLastPipeline.

        流水线状态

        :param status: The status of this SpecificCommitInfoLastPipeline.
        :type status: str
        """
        self._status = status

    @property
    def web_url(self):
        """Gets the web_url of this SpecificCommitInfoLastPipeline.

        流水线url

        :return: The web_url of this SpecificCommitInfoLastPipeline.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this SpecificCommitInfoLastPipeline.

        流水线url

        :param web_url: The web_url of this SpecificCommitInfoLastPipeline.
        :type web_url: str
        """
        self._web_url = web_url

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
        if not isinstance(other, SpecificCommitInfoLastPipeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

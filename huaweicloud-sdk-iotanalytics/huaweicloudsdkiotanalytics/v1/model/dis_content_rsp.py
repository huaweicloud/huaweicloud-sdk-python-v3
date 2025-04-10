# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisContentRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'ak': 'str',
        'sk': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'stream_name': 'streamName',
        'ak': 'ak',
        'sk': 'sk',
        'project_id': 'projectId'
    }

    def __init__(self, stream_name=None, ak=None, sk=None, project_id=None):
        r"""DisContentRsp

        The model defined in huaweicloud sdk

        :param stream_name: 通道名称
        :type stream_name: str
        :param ak: 租户的AK
        :type ak: str
        :param sk: 租户的SK
        :type sk: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._stream_name = None
        self._ak = None
        self._sk = None
        self._project_id = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if project_id is not None:
            self.project_id = project_id

    @property
    def stream_name(self):
        r"""Gets the stream_name of this DisContentRsp.

        通道名称

        :return: The stream_name of this DisContentRsp.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this DisContentRsp.

        通道名称

        :param stream_name: The stream_name of this DisContentRsp.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def ak(self):
        r"""Gets the ak of this DisContentRsp.

        租户的AK

        :return: The ak of this DisContentRsp.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this DisContentRsp.

        租户的AK

        :param ak: The ak of this DisContentRsp.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this DisContentRsp.

        租户的SK

        :return: The sk of this DisContentRsp.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this DisContentRsp.

        租户的SK

        :param sk: The sk of this DisContentRsp.
        :type sk: str
        """
        self._sk = sk

    @property
    def project_id(self):
        r"""Gets the project_id of this DisContentRsp.

        项目id

        :return: The project_id of this DisContentRsp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DisContentRsp.

        项目id

        :param project_id: The project_id of this DisContentRsp.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, DisContentRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

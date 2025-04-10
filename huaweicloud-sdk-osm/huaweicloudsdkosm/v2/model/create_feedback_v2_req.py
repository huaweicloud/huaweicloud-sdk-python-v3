# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFeedbackV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'title': 'str',
        'content': 'str',
        'files': 'list[str]',
        'ip': 'IntellectualPropertyV2',
        'contacts': 'ContactWayInfoV2'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'content': 'content',
        'files': 'files',
        'ip': 'ip',
        'contacts': 'contacts'
    }

    def __init__(self, type=None, title=None, content=None, files=None, ip=None, contacts=None):
        r"""CreateFeedbackV2Req

        The model defined in huaweicloud sdk

        :param type: 举报类型
        :type type: str
        :param title: 涉案的华为云产品或服务; 举报网址
        :type title: str
        :param content: 侵权详情说明或举报内容及说明
        :type content: str
        :param files: 相关证明附件列表
        :type files: list[str]
        :param ip: 
        :type ip: :class:`huaweicloudsdkosm.v2.IntellectualPropertyV2`
        :param contacts: 
        :type contacts: :class:`huaweicloudsdkosm.v2.ContactWayInfoV2`
        """
        
        

        self._type = None
        self._title = None
        self._content = None
        self._files = None
        self._ip = None
        self._contacts = None
        self.discriminator = None

        self.type = type
        self.title = title
        self.content = content
        self.files = files
        if ip is not None:
            self.ip = ip
        self.contacts = contacts

    @property
    def type(self):
        r"""Gets the type of this CreateFeedbackV2Req.

        举报类型

        :return: The type of this CreateFeedbackV2Req.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateFeedbackV2Req.

        举报类型

        :param type: The type of this CreateFeedbackV2Req.
        :type type: str
        """
        self._type = type

    @property
    def title(self):
        r"""Gets the title of this CreateFeedbackV2Req.

        涉案的华为云产品或服务; 举报网址

        :return: The title of this CreateFeedbackV2Req.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateFeedbackV2Req.

        涉案的华为云产品或服务; 举报网址

        :param title: The title of this CreateFeedbackV2Req.
        :type title: str
        """
        self._title = title

    @property
    def content(self):
        r"""Gets the content of this CreateFeedbackV2Req.

        侵权详情说明或举报内容及说明

        :return: The content of this CreateFeedbackV2Req.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateFeedbackV2Req.

        侵权详情说明或举报内容及说明

        :param content: The content of this CreateFeedbackV2Req.
        :type content: str
        """
        self._content = content

    @property
    def files(self):
        r"""Gets the files of this CreateFeedbackV2Req.

        相关证明附件列表

        :return: The files of this CreateFeedbackV2Req.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this CreateFeedbackV2Req.

        相关证明附件列表

        :param files: The files of this CreateFeedbackV2Req.
        :type files: list[str]
        """
        self._files = files

    @property
    def ip(self):
        r"""Gets the ip of this CreateFeedbackV2Req.

        :return: The ip of this CreateFeedbackV2Req.
        :rtype: :class:`huaweicloudsdkosm.v2.IntellectualPropertyV2`
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CreateFeedbackV2Req.

        :param ip: The ip of this CreateFeedbackV2Req.
        :type ip: :class:`huaweicloudsdkosm.v2.IntellectualPropertyV2`
        """
        self._ip = ip

    @property
    def contacts(self):
        r"""Gets the contacts of this CreateFeedbackV2Req.

        :return: The contacts of this CreateFeedbackV2Req.
        :rtype: :class:`huaweicloudsdkosm.v2.ContactWayInfoV2`
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        r"""Sets the contacts of this CreateFeedbackV2Req.

        :param contacts: The contacts of this CreateFeedbackV2Req.
        :type contacts: :class:`huaweicloudsdkosm.v2.ContactWayInfoV2`
        """
        self._contacts = contacts

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
        if not isinstance(other, CreateFeedbackV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

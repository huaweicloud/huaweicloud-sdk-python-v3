# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateObjectReplicationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_info': 'ObsInfo',
        'file_type': 'str',
        'dest_info': 'ObsInfo',
        'category_id': 'object',
        'callback_url': 'str',
        'session_context': 'str'
    }

    attribute_map = {
        'src_info': 'src_info',
        'file_type': 'file_type',
        'dest_info': 'dest_info',
        'category_id': 'category_id',
        'callback_url': 'callback_url',
        'session_context': 'session_context'
    }

    def __init__(self, src_info=None, file_type=None, dest_info=None, category_id=None, callback_url=None, session_context=None):
        r"""CreateObjectReplicationRequestBody

        The model defined in huaweicloud sdk

        :param src_info: 
        :type src_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param file_type: 源文件类型
        :type file_type: str
        :param dest_info: 
        :type dest_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param category_id: 媒资分类id
        :type category_id: object
        :param callback_url: 回调地址，为空则不回调
        :type callback_url: str
        :param session_context: 自定义上下文，回调时会回调给用户，透传信息
        :type session_context: str
        """
        
        

        self._src_info = None
        self._file_type = None
        self._dest_info = None
        self._category_id = None
        self._callback_url = None
        self._session_context = None
        self.discriminator = None

        self.src_info = src_info
        if file_type is not None:
            self.file_type = file_type
        self.dest_info = dest_info
        if category_id is not None:
            self.category_id = category_id
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context

    @property
    def src_info(self):
        r"""Gets the src_info of this CreateObjectReplicationRequestBody.

        :return: The src_info of this CreateObjectReplicationRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._src_info

    @src_info.setter
    def src_info(self, src_info):
        r"""Sets the src_info of this CreateObjectReplicationRequestBody.

        :param src_info: The src_info of this CreateObjectReplicationRequestBody.
        :type src_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._src_info = src_info

    @property
    def file_type(self):
        r"""Gets the file_type of this CreateObjectReplicationRequestBody.

        源文件类型

        :return: The file_type of this CreateObjectReplicationRequestBody.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this CreateObjectReplicationRequestBody.

        源文件类型

        :param file_type: The file_type of this CreateObjectReplicationRequestBody.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def dest_info(self):
        r"""Gets the dest_info of this CreateObjectReplicationRequestBody.

        :return: The dest_info of this CreateObjectReplicationRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._dest_info

    @dest_info.setter
    def dest_info(self, dest_info):
        r"""Sets the dest_info of this CreateObjectReplicationRequestBody.

        :param dest_info: The dest_info of this CreateObjectReplicationRequestBody.
        :type dest_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._dest_info = dest_info

    @property
    def category_id(self):
        r"""Gets the category_id of this CreateObjectReplicationRequestBody.

        媒资分类id

        :return: The category_id of this CreateObjectReplicationRequestBody.
        :rtype: object
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this CreateObjectReplicationRequestBody.

        媒资分类id

        :param category_id: The category_id of this CreateObjectReplicationRequestBody.
        :type category_id: object
        """
        self._category_id = category_id

    @property
    def callback_url(self):
        r"""Gets the callback_url of this CreateObjectReplicationRequestBody.

        回调地址，为空则不回调

        :return: The callback_url of this CreateObjectReplicationRequestBody.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this CreateObjectReplicationRequestBody.

        回调地址，为空则不回调

        :param callback_url: The callback_url of this CreateObjectReplicationRequestBody.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this CreateObjectReplicationRequestBody.

        自定义上下文，回调时会回调给用户，透传信息

        :return: The session_context of this CreateObjectReplicationRequestBody.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this CreateObjectReplicationRequestBody.

        自定义上下文，回调时会回调给用户，透传信息

        :param session_context: The session_context of this CreateObjectReplicationRequestBody.
        :type session_context: str
        """
        self._session_context = session_context

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
        if not isinstance(other, CreateObjectReplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

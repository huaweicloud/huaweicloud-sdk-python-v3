# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'is_default': 'bool',
        'offset': 'int',
        'limit': 'int',
        'query_string': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'is_default': 'is_default',
        'offset': 'offset',
        'limit': 'limit',
        'query_string': 'query_string'
    }

    def __init__(self, group_id=None, is_default=None, offset=None, limit=None, query_string=None):
        """ListTranscodeTemplateRequest

        The model defined in huaweicloud sdk

        :param group_id: 模板id 
        :type group_id: str
        :param is_default: 是否默认 
        :type is_default: bool
        :param offset: 偏移量。默认为0。指定group_id时该参数无效。&lt;br/&gt; 
        :type offset: int
        :param limit: 每页记录数。默认为10，范围[1,100]。指定group_id时该参数无效。&lt;br/&gt; 
        :type limit: int
        :param query_string: 按照模板名和描述模糊查询。指定group_id时该参数无效。&lt;br/&gt; 
        :type query_string: str
        """
        
        

        self._group_id = None
        self._is_default = None
        self._offset = None
        self._limit = None
        self._query_string = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if is_default is not None:
            self.is_default = is_default
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if query_string is not None:
            self.query_string = query_string

    @property
    def group_id(self):
        """Gets the group_id of this ListTranscodeTemplateRequest.

        模板id 

        :return: The group_id of this ListTranscodeTemplateRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListTranscodeTemplateRequest.

        模板id 

        :param group_id: The group_id of this ListTranscodeTemplateRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def is_default(self):
        """Gets the is_default of this ListTranscodeTemplateRequest.

        是否默认 

        :return: The is_default of this ListTranscodeTemplateRequest.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this ListTranscodeTemplateRequest.

        是否默认 

        :param is_default: The is_default of this ListTranscodeTemplateRequest.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def offset(self):
        """Gets the offset of this ListTranscodeTemplateRequest.

        偏移量。默认为0。指定group_id时该参数无效。<br/> 

        :return: The offset of this ListTranscodeTemplateRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTranscodeTemplateRequest.

        偏移量。默认为0。指定group_id时该参数无效。<br/> 

        :param offset: The offset of this ListTranscodeTemplateRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTranscodeTemplateRequest.

        每页记录数。默认为10，范围[1,100]。指定group_id时该参数无效。<br/> 

        :return: The limit of this ListTranscodeTemplateRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTranscodeTemplateRequest.

        每页记录数。默认为10，范围[1,100]。指定group_id时该参数无效。<br/> 

        :param limit: The limit of this ListTranscodeTemplateRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def query_string(self):
        """Gets the query_string of this ListTranscodeTemplateRequest.

        按照模板名和描述模糊查询。指定group_id时该参数无效。<br/> 

        :return: The query_string of this ListTranscodeTemplateRequest.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this ListTranscodeTemplateRequest.

        按照模板名和描述模糊查询。指定group_id时该参数无效。<br/> 

        :param query_string: The query_string of this ListTranscodeTemplateRequest.
        :type query_string: str
        """
        self._query_string = query_string

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
        if not isinstance(other, ListTranscodeTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

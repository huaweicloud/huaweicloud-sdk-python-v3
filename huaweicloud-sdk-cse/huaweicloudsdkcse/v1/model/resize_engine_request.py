# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeEngineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_project_id': 'str',
        'content_type': 'str',
        'accept': 'str',
        'engine_id': 'str',
        'body': 'EngineModifyReq'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'content_type': 'Content-Type',
        'accept': 'Accept',
        'engine_id': 'engine_id',
        'body': 'body'
    }

    def __init__(self, x_enterprise_project_id=None, content_type=None, accept=None, engine_id=None, body=None):
        r"""ResizeEngineRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_project_id: 如果不带则默认企业项目为\&quot;default\&quot;，ID为\&quot;0\&quot;
        :type x_enterprise_project_id: str
        :param content_type: 该字段内容填为 \&quot;application/json;charset&#x3D;UTF-8\&quot;
        :type content_type: str
        :param accept: 该字段内容填为 \&quot;application/json\&quot;
        :type accept: str
        :param engine_id: 引擎id
        :type engine_id: str
        :param body: Body of the ResizeEngineRequest
        :type body: :class:`huaweicloudsdkcse.v1.EngineModifyReq`
        """
        
        

        self._x_enterprise_project_id = None
        self._content_type = None
        self._accept = None
        self._engine_id = None
        self._body = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        self.content_type = content_type
        self.accept = accept
        self.engine_id = engine_id
        if body is not None:
            self.body = body

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this ResizeEngineRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"

        :return: The x_enterprise_project_id of this ResizeEngineRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this ResizeEngineRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"

        :param x_enterprise_project_id: The x_enterprise_project_id of this ResizeEngineRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def content_type(self):
        r"""Gets the content_type of this ResizeEngineRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"

        :return: The content_type of this ResizeEngineRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ResizeEngineRequest.

        该字段内容填为 \"application/json;charset=UTF-8\"

        :param content_type: The content_type of this ResizeEngineRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def accept(self):
        r"""Gets the accept of this ResizeEngineRequest.

        该字段内容填为 \"application/json\"

        :return: The accept of this ResizeEngineRequest.
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        r"""Sets the accept of this ResizeEngineRequest.

        该字段内容填为 \"application/json\"

        :param accept: The accept of this ResizeEngineRequest.
        :type accept: str
        """
        self._accept = accept

    @property
    def engine_id(self):
        r"""Gets the engine_id of this ResizeEngineRequest.

        引擎id

        :return: The engine_id of this ResizeEngineRequest.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this ResizeEngineRequest.

        引擎id

        :param engine_id: The engine_id of this ResizeEngineRequest.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def body(self):
        r"""Gets the body of this ResizeEngineRequest.

        :return: The body of this ResizeEngineRequest.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineModifyReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ResizeEngineRequest.

        :param body: The body of this ResizeEngineRequest.
        :type body: :class:`huaweicloudsdkcse.v1.EngineModifyReq`
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
        if not isinstance(other, ResizeEngineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

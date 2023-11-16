# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeEngineConfigRequest:

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
        'engine_id': 'str',
        'body': 'EngineConfigureReq'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'engine_id': 'engine_id',
        'body': 'body'
    }

    def __init__(self, x_enterprise_project_id=None, engine_id=None, body=None):
        """UpgradeEngineConfigRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_project_id: 如果不带则默认企业项目为\&quot;default\&quot;，ID为\&quot;0\&quot;
        :type x_enterprise_project_id: str
        :param engine_id: 更新的引擎Id
        :type engine_id: str
        :param body: Body of the UpgradeEngineConfigRequest
        :type body: :class:`huaweicloudsdkcse.v1.EngineConfigureReq`
        """
        
        

        self._x_enterprise_project_id = None
        self._engine_id = None
        self._body = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        self.engine_id = engine_id
        if body is not None:
            self.body = body

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this UpgradeEngineConfigRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"

        :return: The x_enterprise_project_id of this UpgradeEngineConfigRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this UpgradeEngineConfigRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"

        :param x_enterprise_project_id: The x_enterprise_project_id of this UpgradeEngineConfigRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def engine_id(self):
        """Gets the engine_id of this UpgradeEngineConfigRequest.

        更新的引擎Id

        :return: The engine_id of this UpgradeEngineConfigRequest.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this UpgradeEngineConfigRequest.

        更新的引擎Id

        :param engine_id: The engine_id of this UpgradeEngineConfigRequest.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def body(self):
        """Gets the body of this UpgradeEngineConfigRequest.

        :return: The body of this UpgradeEngineConfigRequest.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineConfigureReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpgradeEngineConfigRequest.

        :param body: The body of this UpgradeEngineConfigRequest.
        :type body: :class:`huaweicloudsdkcse.v1.EngineConfigureReq`
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
        if not isinstance(other, UpgradeEngineConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgenciesTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'operate_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'operate_type': 'operate_type'
    }

    def __init__(self, project_id=None, operate_type=None):
        """AgenciesTaskReq

        The model defined in huaweicloud sdk

        :param project_id: 委托任务租户Id
        :type project_id: str
        :param operate_type: 操作标记，取值[CREATED,CANCELED]，CREATED表示授权, CANCELED表示取消授权 
        :type operate_type: str
        """
        
        

        self._project_id = None
        self._operate_type = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        self.operate_type = operate_type

    @property
    def project_id(self):
        """Gets the project_id of this AgenciesTaskReq.

        委托任务租户Id

        :return: The project_id of this AgenciesTaskReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AgenciesTaskReq.

        委托任务租户Id

        :param project_id: The project_id of this AgenciesTaskReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def operate_type(self):
        """Gets the operate_type of this AgenciesTaskReq.

        操作标记，取值[CREATED,CANCELED]，CREATED表示授权, CANCELED表示取消授权 

        :return: The operate_type of this AgenciesTaskReq.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this AgenciesTaskReq.

        操作标记，取值[CREATED,CANCELED]，CREATED表示授权, CANCELED表示取消授权 

        :param operate_type: The operate_type of this AgenciesTaskReq.
        :type operate_type: str
        """
        self._operate_type = operate_type

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
        if not isinstance(other, AgenciesTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

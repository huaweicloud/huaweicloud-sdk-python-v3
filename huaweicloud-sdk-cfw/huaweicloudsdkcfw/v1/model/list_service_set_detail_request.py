# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceSetDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'set_id': 'set_id',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, set_id=None, enterprise_project_id=None, fw_instance_id=None):
        """ListServiceSetDetailRequest

        The model defined in huaweicloud sdk

        :param set_id: 服务组id
        :type set_id: str
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。
        :type fw_instance_id: str
        """
        
        

        self._set_id = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self.discriminator = None

        self.set_id = set_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id

    @property
    def set_id(self):
        """Gets the set_id of this ListServiceSetDetailRequest.

        服务组id

        :return: The set_id of this ListServiceSetDetailRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ListServiceSetDetailRequest.

        服务组id

        :param set_id: The set_id of this ListServiceSetDetailRequest.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListServiceSetDetailRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :return: The enterprise_project_id of this ListServiceSetDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListServiceSetDetailRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :param enterprise_project_id: The enterprise_project_id of this ListServiceSetDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this ListServiceSetDetailRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :return: The fw_instance_id of this ListServiceSetDetailRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this ListServiceSetDetailRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :param fw_instance_id: The fw_instance_id of this ListServiceSetDetailRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, ListServiceSetDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

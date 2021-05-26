# coding: utf-8

import pprint
import re

import six





class CreateCloudPersistentVolumeClaimsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'x_cluster_id': 'str',
        'body': 'PersistentVolumeClaim'
    }

    attribute_map = {
        'namespace': 'namespace',
        'x_cluster_id': 'X-Cluster-ID',
        'body': 'body'
    }

    def __init__(self, namespace=None, x_cluster_id=None, body=None):
        """CreateCloudPersistentVolumeClaimsRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._x_cluster_id = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        if x_cluster_id is not None:
            self.x_cluster_id = x_cluster_id
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        """Gets the namespace of this CreateCloudPersistentVolumeClaimsRequest.

        Namespace是对一组资源和对象的抽象集合，用来将系统内部的对象划分为不同的项目组或用户组。以小写字母开头，由小写字母、数字、中划线（-）组成，且不能以中划线（-）结尾。  使用namespace有如下约束：  - 用户自定义的namespace，使用前必须先[[创建Namespace](https://support.huaweicloud.com/api-cce/cce_02_0050.html)](tag:hws)[[创建Namespace](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0050.html)](tag:hws_hk)  - 系统自带的namespace：default  - 不能使用kube-system与kube-public 

        :return: The namespace of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CreateCloudPersistentVolumeClaimsRequest.

        Namespace是对一组资源和对象的抽象集合，用来将系统内部的对象划分为不同的项目组或用户组。以小写字母开头，由小写字母、数字、中划线（-）组成，且不能以中划线（-）结尾。  使用namespace有如下约束：  - 用户自定义的namespace，使用前必须先[[创建Namespace](https://support.huaweicloud.com/api-cce/cce_02_0050.html)](tag:hws)[[创建Namespace](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0050.html)](tag:hws_hk)  - 系统自带的namespace：default  - 不能使用kube-system与kube-public 

        :param namespace: The namespace of this CreateCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def x_cluster_id(self):
        """Gets the x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.

        集群ID，使用**https://Endpoint/uri**这种URL格式时必须指定此参数。获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :return: The x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._x_cluster_id

    @x_cluster_id.setter
    def x_cluster_id(self, x_cluster_id):
        """Sets the x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.

        集群ID，使用**https://Endpoint/uri**这种URL格式时必须指定此参数。获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :param x_cluster_id: The x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._x_cluster_id = x_cluster_id

    @property
    def body(self):
        """Gets the body of this CreateCloudPersistentVolumeClaimsRequest.


        :return: The body of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: PersistentVolumeClaim
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateCloudPersistentVolumeClaimsRequest.


        :param body: The body of this CreateCloudPersistentVolumeClaimsRequest.
        :type: PersistentVolumeClaim
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCloudPersistentVolumeClaimsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

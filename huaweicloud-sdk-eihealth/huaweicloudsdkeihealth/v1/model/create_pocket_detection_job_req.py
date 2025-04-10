# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePocketDetectionJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CreateDrugJobBasicInfo',
        'receptor': 'ReceptorDrugFile',
        'ligand': 'ProbeDrugFile',
        'params': 'PocketDetectionParamDto'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'ligand': 'ligand',
        'params': 'params'
    }

    def __init__(self, basic_info=None, receptor=None, ligand=None, params=None):
        r"""CreatePocketDetectionJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param ligand: 
        :type ligand: :class:`huaweicloudsdkeihealth.v1.ProbeDrugFile`
        :param params: 
        :type params: :class:`huaweicloudsdkeihealth.v1.PocketDetectionParamDto`
        """
        
        

        self._basic_info = None
        self._receptor = None
        self._ligand = None
        self._params = None
        self.discriminator = None

        self.basic_info = basic_info
        self.receptor = receptor
        self.ligand = ligand
        if params is not None:
            self.params = params

    @property
    def basic_info(self):
        r"""Gets the basic_info of this CreatePocketDetectionJobReq.

        :return: The basic_info of this CreatePocketDetectionJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this CreatePocketDetectionJobReq.

        :param basic_info: The basic_info of this CreatePocketDetectionJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        r"""Gets the receptor of this CreatePocketDetectionJobReq.

        :return: The receptor of this CreatePocketDetectionJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this CreatePocketDetectionJobReq.

        :param receptor: The receptor of this CreatePocketDetectionJobReq.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._receptor = receptor

    @property
    def ligand(self):
        r"""Gets the ligand of this CreatePocketDetectionJobReq.

        :return: The ligand of this CreatePocketDetectionJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ProbeDrugFile`
        """
        return self._ligand

    @ligand.setter
    def ligand(self, ligand):
        r"""Sets the ligand of this CreatePocketDetectionJobReq.

        :param ligand: The ligand of this CreatePocketDetectionJobReq.
        :type ligand: :class:`huaweicloudsdkeihealth.v1.ProbeDrugFile`
        """
        self._ligand = ligand

    @property
    def params(self):
        r"""Gets the params of this CreatePocketDetectionJobReq.

        :return: The params of this CreatePocketDetectionJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PocketDetectionParamDto`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreatePocketDetectionJobReq.

        :param params: The params of this CreatePocketDetectionJobReq.
        :type params: :class:`huaweicloudsdkeihealth.v1.PocketDetectionParamDto`
        """
        self._params = params

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
        if not isinstance(other, CreatePocketDetectionJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
